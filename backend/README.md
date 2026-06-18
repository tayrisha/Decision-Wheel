# Decision Wheel — Backend

FastAPI API for decision scoring and support.

## Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (recommended) or `venv` + `pip`

## Setup

```powershell
cd backend
uv venv
uv sync --extra dev
```

## Run (after app skeleton is added)

```powershell
uv run uvicorn app.main:app --reload
```

## Test / lint

```powershell
uv run pytest
uv run ruff check .
uv run black --check .
```
