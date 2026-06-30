"""환경 변수 기반 설정. `.env`에서 로드한다 (`.env.example` 참고)."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # LLM
    llm_model: str = "ollama/qwen2.5:7b-instruct"
    llm_api_base: str = "http://localhost:11434"
    openai_api_key: str = ""
    anthropic_api_key: str = ""

    # Embeddings
    embed_model: str = "ollama/bge-m3"
    embed_dim: int = 1024

    # Qdrant
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "papers"

    # Neo4j
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "password123"

    # Semantic Scholar
    semantic_scholar_api_key: str = ""

    # Corpus
    arxiv_categories: str = "cs.CL,cs.AI"
    arxiv_year_min: int = 2022
    arxiv_year_max: int = 2025

    @property
    def categories(self) -> list[str]:
        return [c.strip() for c in self.arxiv_categories.split(",") if c.strip()]


settings = Settings()
