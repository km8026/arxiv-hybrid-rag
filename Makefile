.PHONY: up down logs install ingest citations index graph demo eval

# ---- Infra ----
up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

# ---- Setup ----
install:
	pip install -r requirements.txt

# ---- Pipeline ----
ingest:
	python -m src.ingest.arxiv_loader

citations:
	python -m src.ingest.citations

index:
	python -m src.index.qdrant_store

graph:
	python -m src.graph.neo4j_store

# ---- Run ----
demo:
	python -m src.api.demo

eval:
	python eval/run_ragas.py
