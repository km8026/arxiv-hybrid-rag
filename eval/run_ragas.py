"""[Phase 3] RAGAS 평가 — 구성별 before-after 비교.

testset.jsonl(50문항)에 대해 vector / hybrid / +graphrag / +rerank 구성을
각각 실행하고 faithfulness, answer relevancy, context precision/recall을 측정한다.
결과표는 README에 게재.
"""
from __future__ import annotations

CONFIGS = ["vector", "hybrid", "graphrag", "rerank"]


def main() -> None:
    raise NotImplementedError("Phase 3: 구성별 실행 + RAGAS 측정 + 비교표 출력")


if __name__ == "__main__":
    main()
