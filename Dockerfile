FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
ENV UV_SYSTEM_PYTHON=1
ENV UV_COMPILE_BYTECODE=1

WORKDIR /app
COPY pyproject.toml .

RUN uv pip install -r pyproject.toml
COPY . .

RUN uv pip install -e .
CMD ["fastapi", "run", "run.py", "--port", "80", "--workers", "8"]
