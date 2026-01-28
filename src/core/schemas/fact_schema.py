from __future__ import annotations

from typing import Literal, Optional
from pydantic import BaseModel, Field


# -------------------------
# Evidence schema
# -------------------------

class FactEvidence(BaseModel):
    transcript_key: str = Field(
        ...,
        description="Key of the transcript in SessionState.transcripts",
    )
    transcript_file: Optional[str] = Field(
        None,
        description="Original transcript filename (for traceability)",
    )
    chunk_id: int = Field(
        ...,
        description="Chunk index within the transcript",
    )
    quote: Optional[str] = Field(
        None,
        description="Short supporting quote (<=200 chars)",
    )
    anchor: Optional[str] = Field(
        None,
        description="Optional anchor like timestamp, page, or keyword",
    )


# -------------------------
# Fact schema
# -------------------------

class Fact(BaseModel):
    """
    Atomic, evidence-backed fact extracted from transcripts or knowledge sources.
    """

    type: Literal[
        "OBJECTIVE",
        "PROBLEM",
        "KPI",
        "WORKFLOW",
        "WORKFLOW_STEP",
        "PAIN_POINT",
        "SYSTEM",
        "INTEGRATION_TARGET",
        "DATA_SOURCE",
        "DATA_QUALITY",
        "DATA_VOLUME",
        "ACCESS_CONSTRAINT",
        "TIMELINE",
        "MILESTONE",
        "PHASE",
        "RESOURCE",
        "COST_CAPEX",
        "COST_OPEX",
        "PRICING_MODEL",
        "ROI_ASSUMPTION",
        "RISK",
        "MITIGATION",
        "DECISION",
        "ACTION_ITEM",
        "OPEN_QUESTION",
        "OTHER",
    ] = Field(
        ...,
        description="Semantic category of the fact",
    )

    value: str = Field(
        ...,
        description="Atomic factual statement",
        min_length=1,
    )

    confidence: Literal[
        "HIGH",
        "MEDIUM",
        "LOW",
    ] = Field(
        "LOW",
        description="Confidence level based on explicitness in transcript",
    )

    evidence: FactEvidence = Field(
        ...,
        description="Traceability information for this fact",
    )
