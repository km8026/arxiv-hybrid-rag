"""공용 데이터 타입."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Paper:
    arxiv_id: str
    title: str
    abstract: str
    authors: list[str] = field(default_factory=list)
    categories: list[str] = field(default_factory=list)
    primary_category: str = ""
    year: int | None = None
    doi: str = ""
    journal_ref: str = ""
    # Semantic Scholar 보강 (Phase 2)
    cites: list[str] = field(default_factory=list)  # 이 논문이 인용한 arxiv_id 목록


@dataclass
class RetrievedDoc:
    arxiv_id: str
    title: str
    text: str
    score: float
    source: str  # "vector" | "graph" | "hybrid" | "graphrag"
