"""[Phase 1] Qdrant 벡터 검색 (정형 메타 필터 지원)."""
from __future__ import annotations

from ..models import RetrievedDoc


def search(
    query: str,
    top_k: int = 10,
    category: str | None = None,
    year_min: int | None = None,
    year_max: int | None = None,
) -> list[RetrievedDoc]:
    """질의 임베딩으로 유사 논문 검색. category/year로 payload 필터."""
    raise NotImplementedError("Phase 1: 임베딩 검색 + payload 필터")
