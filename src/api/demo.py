"""[Phase 1] CLI 데모 — 파이프라인 전체를 한 줄 질의로 실행.

흐름: 입력 가드레일 → 라우팅 → 검색 → (재정렬) → 답변 생성 → 출력 가드레일.
"""
from __future__ import annotations

import sys

from ..generate.answer import answer
from ..guardrails.checks import check_input, check_output
from ..retrieve import hybrid, vector_search
from ..retrieve.router import Route, route


def ask(question: str) -> str:
    ok, reason = check_input(question)
    if not ok:
        return f"[거부] {reason}"

    r = route(question)
    docs = hybrid.search(question) if r == Route.HYBRID else vector_search.search(question)

    result = answer(question, docs)
    ok, reason = check_output(result, docs)
    return result if ok else f"[보류] {reason}"


def main() -> None:
    question = " ".join(sys.argv[1:]) or "What is retrieval-augmented generation?"
    print(ask(question))


if __name__ == "__main__":
    main()
