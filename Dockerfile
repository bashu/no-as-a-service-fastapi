FROM docker.io/python:3.14-slim
COPY --from=ghcr.io/astral-sh/uv:0.12 /uv /bin/uv

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_NO_DEV=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-install-project && rm /bin/uv
COPY main.py reasons.json ./

RUN useradd --system --no-create-home app
USER app
EXPOSE 8000

CMD ["fastapi", "run", "main.py", "--forwarded-allow-ips", "*"]
