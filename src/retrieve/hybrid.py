"""[Phase 2] 하이브리드 검색 — 벡터 검색 후 그래프로 확장·융합.

흐름: vector_search로 시드 논문 → Neo4j로 인용/저자 이웃 확장
      → 점수 융합 → 통합 컨텍스트 반환.
"""
from __future__ import annotations

from ..models import RetrievedDoc


def search(query: str, top_k: int = 10) -> list[RetrievedDoc]:
    """벡터 시드 + 그래프 확장 결과를 융합해 반환."""
    raise NotImplementedError("Phase 2: 벡터 시드 → 그래프 확장 → 점수 융합")
