"""[Phase 1] 입출력 가드레일.

입력: 주제 범위(CS/AI 논문 질의) 검사, 프롬프트 인젝션/과길이 차단.
출력: 출처(arxiv_id) 인용 강제, 낮은 점수 시 추상, 코퍼스 미존재 ID 환각 차단.
"""
from __future__ import annotations

from ..models import RetrievedDoc


def check_input(question: str) -> tuple[bool, str]:
    """(통과 여부, 사유). 통과 시 (True, "")."""
    raise NotImplementedError("Phase 1: 입력 가드레일")


def check_output(answer: str, used_docs: list[RetrievedDoc]) -> tuple[bool, str]:
    """답변의 출처 인용·환각 검증. (통과 여부, 사유)."""
    raise NotImplementedError("Phase 1: 출력 가드레일 (출처/환각 검증)")
