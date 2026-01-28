from src.core.tools.supabase_db import supabase
from pathlib import Path
from typing import Dict, Any
from datetime import datetime

from src.core.state import SessionState, SectionRef

#---------------------------------------------------------------
# Helper functions to fetch data from Supabase
#---------------------------------------------------------------


# Fetch section timestamps and contents from Supabase

async def fetch_section_timestamps(
    opportunity_id: str,
    report_type: str,
):
    """
    Returns: id, title, updated_at for all sections
    belonging to documents of the given opportunity id and report type.
    """

    return (
        supabase
        .from_("document_sections")
        .select(
            "id, title, last_edited_at, document_id, "
            "documents!inner(type)"
        )
        .eq("documents.type", report_type)
        .eq("documents.opportunity_id", opportunity_id)
        .execute()
    )



# Fetch sections by IDs
from langgraph.types import RunnableConfig

async def fetch_sections_by_ids(section_names: list[str]):
    return (
        supabase
        .from_("document_sections")
        .select("id, title, content, last_edited_at")
        .in_("title", section_names)
        .execute()
    )


def _to_epoch(ts) -> float:
    if isinstance(ts, str):
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp()
    return ts.timestamp()


async def ensure_completed_sections_synced(
    state: SessionState,
    config: RunnableConfig,
    
) -> Dict[str, Any]:
    
    print("Syncing completed sections from DB...")
    
    # Define local storage directory for sections
    SECTIONS_DIR = Path(".temp/sections")
    
    """
    Sync completed sections from DB to local cache + state.
    Steps:
    - Compare per-section updated_at with last fetched timestamp
    - Fetch only sections that changed
    """
    cfg = config["configurable"]

    opportunity_id = cfg["opportunity_id"]
    report_type = cfg["report_type"]
    SECTIONS_DIR.mkdir(parents=True, exist_ok=True)

    # Fetch section timestamps from DB
    resp = await fetch_section_timestamps(opportunity_id, report_type)
    rows = resp.data or []

    if not rows:
        return {}

    #  Determine which sections are fresh
    to_fetch: list[str] = []

    for r in rows:
        section_id = r["id"]
        last_edited_at = _to_epoch(r["last_edited_at"])

        last_fetched = state.completed_sections_fetched_at.get(section_id)

        if last_fetched is None or last_edited_at > last_fetched:
            to_fetch.append(section_id)

    if not to_fetch:
        return {}

    #  Fetch full content for fresh sections only
    resp = await fetch_sections_by_ids(to_fetch)
    section_rows = resp.data or []

    new_sections: Dict[str, SectionRef] = {}
    new_fetched_at = dict(state.completed_sections_fetched_at)

    for r in section_rows:
        section_id = r["id"]
        title = r["title"]
        content = r["content"]
        updated_at = _to_epoch(r["updated_at"])

        path = SECTIONS_DIR / f"{state.session_id}_{title}.md"
        path.write_text(content or "", encoding="utf-8")

        new_sections[title] = SectionRef(
            section_id=section_id,
            key=title,
            path=str(path),
            updated_at=updated_at,
            source="human",
        )

        new_fetched_at[section_id] = updated_at

    # Merge into state
    merged_sections = dict(state.completed_sections)
    merged_sections.update(new_sections)

    return {
        "completed_sections": merged_sections,
        "completed_sections_fetched_at": new_fetched_at,
    }


