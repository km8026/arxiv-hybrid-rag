"""[Phase 2] Neo4j 메타·인용 그래프 구축.

노드: Paper, Author, Category
엣지: AUTHORED, IN_CATEGORY, CITES(Semantic Scholar 보강)
GPU 불필요 — 결정적 변환.
"""
from __future__ import annotations

from collections.abc import Iterable

from ..models import Paper


def ensure_constraints() -> None:
    """유니크 제약/인덱스 생성 (Paper.arxiv_id, Author.name, Category.code)."""
    raise NotImplementedError("Phase 2: 제약/인덱스 생성")


def build_graph(papers: Iterable[Paper]) -> None:
    """Paper/Author/Category 노드 + AUTHORED/IN_CATEGORY/CITES 엣지 적재."""
    raise NotImplementedError("Phase 2: 노드/엣지 적재 (CITES 포함)")


def main() -> None:
    from ..ingest.arxiv_loader import load_papers

    ensure_constraints()
    build_graph(load_papers())
    print("graph build complete")


if __name__ == "__main__":
    main()
