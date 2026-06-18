# Decision Wheel — Backend

FastAPI backend for the Decision Wheel application. It provides decision-scoring APIs, random selection mode, and future decision history functionality.

> See the [project README](../README.md) for the full stack and product overview.

All commands below assume you are in the `backend/` directory.

## Project structure

```text
backend/
├── app/
│   ├── main.py              # FastAPI app, health routes, router wiring
│   ├── core/
│   │   └── scoring.py       # Pure scoring logic (no FastAPI imports)
│   ├── schemas/
│   │   └── score.py         # Pydantic request/response models
│   └── api/v1/
│       └── score.py         # HTTP routes under /api/v1
├── tests/
│   ├── test_api.py          # Health and readiness endpoint tests
│   └── test_scoring.py      # Scoring logic tests
├── pyproject.toml           # Dependencies and tool config
└── uv.lock                  # Locked dependency versions
```

**Conventions**

- `core/` — business logic only; easy to unit test in isolation.
- `schemas/` — API input/output shapes (Pydantic).
- `api/` — HTTP layer; calls into `core/`.

## Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) — install with `py -m pip install uv`

On Windows, `uv` may not be on PATH after a pip install. Use **`py -m uv`** instead of `uv` in the commands below.

## Quick start

```powershell
cd backend
py -m uv venv
py -m uv sync --extra dev
py -m uv run uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs for the interactive API explorer.


## API

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Liveness check |
| GET | `/ready` | Readiness check |
| GET | `/docs` | OpenAPI explorer (Swagger UI) |

Scoring endpoint (`POST /api/v1/score`) — coming in the next stage.

## Development

```powershell
py -m uv run pytest
py -m uv run ruff check .
py -m uv run black --check .
```

Format code:

```powershell
py -m uv run ruff check --fix .
py -m uv run black .
```

## Troubleshooting

| Error | Cause | Fix |
|-------|--------|-----|
| `'uv' is not recognized` | `uv` not on PATH (pip install) | Use `py -m uv` instead of `uv` |
| `WinError 10048` / port in use | Old server still running on 8000 | Stop it (see below) or use `--port 8001` |
| `WinError 10013` | Port blocked or already taken | Try another port; stop stale `python` on 8000 |
| `Could not import module "app.main"` | Wrong working directory | `cd backend` first |

Find what is using port 8000:

```powershell
netstat -ano | findstr ":8000"
```

Stop that process (replace `PID` with the number from the last column):

```powershell
Stop-Process -Id PID -Force
```

Or use a different port:

```powershell
py -m uv run uvicorn app.main:app --reload --port 8001
```
