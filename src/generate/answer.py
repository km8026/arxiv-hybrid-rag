"""[Phase 1] 검색 컨텍스트 기반 답변 생성.

검색된 문서를 컨텍스트로 구성하고, 출처(arxiv_id) 인용을 강제하는
프롬프트로 LLM 답변을 생성한다.
"""
from __future__ import annotations

from ..llm import complete
from ..models import RetrievedDoc


def build_prompt(question: str, docs: list[RetrievedDoc]) -> list[dict]:
    """출처 인용을 강제하는 메시지 구성."""
    raise NotImplementedError("Phase 1: 컨텍스트 + 인용 강제 프롬프트")


def answer(question: str, docs: list[RetrievedDoc]) -> str:
    """문서 컨텍스트로 답변 생성."""
    return complete(build_prompt(question, docs))
