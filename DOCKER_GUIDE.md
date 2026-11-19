# Docker quickstart

This is an educational container. Docker must be available locally or inside your Codespace.

```bash
docker build -t log-validation-api .
docker run --rm -p 8000:8000 log-validation-api
```

Run tests first with `python3 -m unittest discover -s tests -v`. The CI workflow builds this image automatically after tests pass. Do not put secrets into images.
