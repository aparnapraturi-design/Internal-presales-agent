from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class TextChunk:
    chunk_id: int
    text: str
    start_char: int
    end_char: int


def chunk_text(
    text: str,
    *,
    max_chars: int = 12000,
    overlap_chars: int = 1200,
) -> List[TextChunk]:
    """
    Split text into overlapping character-based chunks.

    - Deterministic
    - Stable chunk_ids
    - Safe for OCR / ASR / long transcripts
    """

    if not text:
        return []

    if overlap_chars >= max_chars:
        raise ValueError("overlap_chars must be smaller than max_chars")

    chunks: List[TextChunk] = []

    text_len = len(text)
    start = 0
    chunk_id = 0

    while start < text_len:
        end = min(start + max_chars, text_len)

        chunk_text = text[start:end]

        chunks.append(
            TextChunk(
                chunk_id=chunk_id,
                text=chunk_text,
                start_char=start,
                end_char=end,
            )
        )

        if end == text_len:
            break

        # move start forward with overlap
        start = end - overlap_chars
        chunk_id += 1

    return chunks
