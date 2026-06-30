"""[Phase 3] cross-encoder 재정렬.

검색 결과를 (query, doc) 쌍으로 cross-encoder 채점해 재정렬한다.
"""
from __future__ import annotations

from ..models import RetrievedDoc


def rerank(query: str, docs: list[RetrievedDoc], top_k: int = 5) -> list[RetrievedDoc]:
    """cross-encoder 점수로 재정렬해 상위 top_k 반환."""
    raise NotImplementedError("Phase 3: cross-encoder(bge-reranker) 재정렬")
