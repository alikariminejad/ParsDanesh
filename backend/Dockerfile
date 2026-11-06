FROM python:3.12-slim-trixie AS builder
COPY uv.lock /app/uv.lock
COPY pyproject.toml /app/pyproject.toml
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
RUN uv sync --locked
ENV PATH="/app/.venv/bin:$PATH"
COPY . .

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app /app
ENV PATH="/app/.venv/bin:$PATH"
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]