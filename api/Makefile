.PHONY: help dev start clean

# Default values
PORT ?= 8000
HOST ?= 0.0.0.0

help:
	@echo "Recall API Commands:"
	@echo "  make dev              - Run development server with auto-reload"
	@echo "  make dev PORT=3000    - Run dev server on custom port"
	@echo "  make start            - Run production server"
	@echo "  make start PORT=8080  - Run production server on custom port"
	@echo "  make clean            - Remove cache and build artifacts"
	@echo ""
	@echo "Variables:"
	@echo "  PORT (default: 8000)  - Port to run server on"
	@echo "  HOST (default: 0.0.0.0) - Host to bind to"

dev:
	uv run fastapi dev src/recall --host $(HOST) --port $(PORT)

start:
	uv run recall --host $(HOST) --port $(PORT)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
# 	rm -rf .pytest_cache .ruff_cache dist build