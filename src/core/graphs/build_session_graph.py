from langgraph.graph import StateGraph, END
from src.core.state import SessionState
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver

from src.core.nodes.context_extractor_node import ensure_context_extracted
from src.core.nodes.section_sync_node import ensure_completed_sections_synced
from src.core.state import SessionState
from src.core.nodes.transcript_loader_node import ensure_transcripts_loaded
from src.core.nodes.config import hydrate_from_config


def build_sessiongraph():
    g = StateGraph(SessionState)

    g.set_entry_point("hydrate")
    g.add_node("hydrate", hydrate_from_config)
    g.add_node("ensure_transcripts_loaded", ensure_transcripts_loaded)
    g.add_node("extract_context", ensure_context_extracted)
    g.add_node("sync_sections", ensure_completed_sections_synced)

    g.add_edge("hydrate", "ensure_transcripts_loaded")
    g.add_edge("ensure_transcripts_loaded", "extract_context")
    g.add_edge("extract_context", "sync_sections")
    g.add_edge("sync_sections", END)

    return g
