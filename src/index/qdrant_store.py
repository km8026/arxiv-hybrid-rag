"""[Phase 1] Qdrant 컬렉션 생성 + 논문 인덱싱.

벡터: bge-m3(1024d) of (title + abstract)
payload: arxiv_id, title, authors, primary_category, categories, year, abstract, doi
payload 인덱스: primary_category, year (정형 필터용)
"""
from __future__ import annotations

from collections.abc import Iterable

from ..config import settings
from ..models import Paper


def ensure_collection() -> None:
    """컬렉션이 없으면 생성 (vector size = settings.embed_dim, payload 인덱스 포함)."""
    raise NotImplementedError("Phase 1: Qdrant 컬렉션 생성 + payload 인덱스")


def index_papers(papers: Iterable[Paper]) -> int:
    """Paper들을 임베딩해 upsert. 인덱싱한 건수 반환."""
    raise NotImplementedError("Phase 1: 임베딩 + upsert")


def main() -> None:
    from ..ingest.arxiv_loader import load_papers

    ensure_collection()
    n = index_papers(load_papers())
    print(f"indexed {n} papers into '{settings.qdrant_collection}'")


if __name__ == "__main__":
    main()
