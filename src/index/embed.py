"""[Phase 1] 임베딩 배치 헬퍼.

실제 임베딩 호출은 src.llm.embed (LiteLLM)에 위임하고, 여기서는 배치/재시도만 담당.
"""
from __future__ import annotations

from ..llm import embed


def embed_batch(texts: list[str], batch_size: int = 32) -> list[list[float]]:
    """텍스트를 batch_size 단위로 나눠 임베딩."""
    raise NotImplementedError("Phase 1: 배치 임베딩 + 진행률 + 재시도")
