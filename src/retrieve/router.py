"""[Phase 2] 질의 유형 라우터.

질의를 vector / graph / global / hybrid 로 분류해 검색 경로를 결정한다.
"""
from __future__ import annotations

from enum import Enum


class Route(str, Enum):
    VECTOR = "vector"      # 사실/의미
    GRAPH = "graph"        # 관계형 (인용·저자·카테고리)
    GLOBAL = "global"      # 글로벌/주제 (GraphRAG 커뮤니티 요약)
    HYBRID = "hybrid"      # 복합 (기본값)


def route(question: str) -> Route:
    """질문을 분석해 검색 경로를 반환."""
    raise NotImplementedError("Phase 2: 규칙/LLM 기반 질의 분류")
