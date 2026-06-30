"""LiteLLM 래퍼 — 프로바이더 무관 생성/임베딩.

`.env`의 LLM_MODEL / EMBED_MODEL만 바꾸면 로컬(Ollama)과 클라우드 API를
코드 수정 없이 교체할 수 있다.
"""
from __future__ import annotations

import litellm

from .config import settings

# 로컬 Ollama 호출 시 api_base만 전달, API 프로바이더는 키를 환경에서 읽음
_LOCAL_PREFIXES = ("ollama/", "ollama_chat/")


def _api_base(model: str) -> str | None:
    return settings.llm_api_base if model.startswith(_LOCAL_PREFIXES) else None


def complete(messages: list[dict], model: str | None = None, **kwargs) -> str:
    """채팅 완성. messages = [{"role": "user", "content": "..."}]."""
    model = model or settings.llm_model
    resp = litellm.completion(
        model=model,
        messages=messages,
        api_base=_api_base(model),
        **kwargs,
    )
    return resp.choices[0].message.content


def embed(texts: list[str], model: str | None = None) -> list[list[float]]:
    """텍스트 리스트 → 임베딩 벡터 리스트."""
    model = model or settings.embed_model
    resp = litellm.embedding(
        model=model,
        input=texts,
        api_base=settings.llm_api_base if model.startswith(_LOCAL_PREFIXES) else None,
    )
    return [item["embedding"] for item in resp.data]
