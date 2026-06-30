"""[Phase 1] Kaggle arXiv 메타데이터(JSONL) 파싱 + 카테고리/연도 서브셋.

데이터: Cornell-University/arxiv (data/arxiv-metadata-oai-snapshot.json)
출력: src.models.Paper 이터레이터
"""
from __future__ import annotations

from collections.abc import Iterator

from ..config import settings
from ..models import Paper


def load_papers(path: str = "data/arxiv-metadata-oai-snapshot.json") -> Iterator[Paper]:
    """JSONL을 스트리밍 파싱해 카테고리/연도 필터를 통과한 Paper만 yield."""
    raise NotImplementedError("Phase 1: Kaggle arXiv JSONL 파싱 + 서브셋 필터")


def main() -> None:
    n = sum(1 for _ in load_papers())
    print(f"loaded {n} papers ({settings.arxiv_categories}, "
          f"{settings.arxiv_year_min}-{settings.arxiv_year_max})")


if __name__ == "__main__":
    main()
