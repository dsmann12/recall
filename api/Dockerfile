FROM python:3.11-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy dependency files first (for better caching)
# Include README.md for uv sync to work properly
COPY pyproject.toml uv.lock*  README.md ./

# Create a minimal src structure for uv sync to work
COPY src/ ./src/

# Install dependencies
RUN uv sync --frozen --no-dev

# Expose port
EXPOSE 8000

# Run using your custom entry point
CMD ["uv", "run", "recall", "--host", "0.0.0.0", "--port", "8000"]