"""Schemas for embedding endpoints."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field, field_validator


def validate_segments(segments):
    if len(segments) > 512 or any(not isinstance(s.get("text"), str) or len(s["text"]) > 20000 for s in segments):
        raise ValueError("At most 512 segments with text strings up to 20000 characters are supported")
    return segments


class SingleTextEmbeddingRequest(BaseModel):
    """Request schema for single text embedding."""

    query: str = Field(max_length=20000)


class ListTextForEmbeddingRequest(BaseModel):
    """Request schema for batch text embedding."""

    segments: List[Dict[str, Any]]
    _validate_segments = field_validator("segments")(validate_segments)


class CompareEmbeddingRequest(BaseModel):
    """Request schema for comparing two embeddings."""

    pattern: str = Field(max_length=20000)
    query: str = Field(max_length=20000)
