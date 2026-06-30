"""[Phase 3] GraphRAG 개념층 — LLM 엔티티/관계 추출 + 커뮤니티 요약.

흐름: 초록 청크 → LLM 개념·관계 추출(MENTIONS) → Leiden 커뮤니티 탐지
      → 커뮤니티별 LLM 요약(Community.summary) → 글로벌 질의에 사용.
LLM 추출이라 GPU 필요. 비용상 소규모 서브셋(예: 2,000편)에만 적용.
"""
from __future__ import annotations

from collections.abc import Iterable

from ..models import Paper


def extract_concepts(papers: Iterable[Paper]) -> None:
    """초록에서 개념/관계 추출 → Concept 노드 + MENTIONS 엣지."""
    raise NotImplementedError("Phase 3: LLM 개념/관계 추출")


def detect_communities() -> None:
    """Leiden으로 커뮤니티 탐지 → IN_COMMUNITY 엣지."""
    raise NotImplementedError("Phase 3: Leiden 커뮤니티 탐지")


def summarize_communities() -> None:
    """커뮤니티별 LLM 요약 → Community.summary."""
    raise NotImplementedError("Phase 3: 커뮤니티 요약")
