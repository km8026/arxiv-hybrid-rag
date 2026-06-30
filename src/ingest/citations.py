"""[Phase 2] Semantic Scholar API로 인용 엣지 보강.

arxivId로 매칭해 references(이 논문이 인용한 논문)를 가져온다.
rate limit 대응: 배치 + 디스크 캐시 + 인용 깊이 1.
"""
from __future__ import annotations

API_BASE = "https://api.semanticscholar.org/graph/v1"


def fetch_references(arxiv_id: str) -> list[str]:
    """주어진 arxiv_id가 인용한 논문들의 arxiv_id 목록을 반환."""
    raise NotImplementedError("Phase 2: Semantic Scholar references 조회 + 캐시")


def main() -> None:
    raise NotImplementedError("Phase 2: 코퍼스 전체 인용 보강 배치")


if __name__ == "__main__":
    main()
