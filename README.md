# Log Validation API

A small FastAPI service that validates **synthetic** telemetry events. No corporate logs or proprietary schemas.

## Run in Codespaces

```bash
python3 -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `/docs` on the forwarded port to try the interactive API.

## Example

`POST /validate` with `{"device_id":"sim-01","timestamp":"2026-11-19T12:00:00Z","severity":"INFO","message":"simulated startup"}`.

## Next exercises

1. Add a batch endpoint.
2. Add tests with `pytest` and `httpx`.
3. Add a Dockerfile and GitHub Actions.

**Status:** Educational starter, not a production API.
