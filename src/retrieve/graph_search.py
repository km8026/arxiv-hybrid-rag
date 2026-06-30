"""[Phase 2] Neo4j Cypher 관계 검색.

예: 특정 논문을 인용한 논문, 저자의 논문, 두 개념을 잇는 경로, 카테고리 내 최다 피인용.
"""
from __future__ import annotations

from ..models import RetrievedDoc


def citing_papers(arxiv_id: str, top_k: int = 10) -> list[RetrievedDoc]:
    """주어진 논문을 인용한 논문들."""
    raise NotImplementedError("Phase 2: CITES 역방향 Cypher")


def by_author(author: str, top_k: int = 10) -> list[RetrievedDoc]:
    """저자의 논문들."""
    raise NotImplementedError("Phase 2: AUTHORED Cypher")
