# Rag API

Web API with endpoints to execute different RAG approches.

## Commands

### Run locally

```bash
uvicorn app.main:app --reload
```

Then access [http://localhost:8000/docs](http://localhost:8000/docs)

### Build & run with Docker

```bash
docker build -t jimmyrl19/rag_api .
docker run -p 8000:8000 jimmyrl19/rag_api
```

## Project structure

Since I'm not a Python developer, I asked ChatGPT a suggested approach for that API.
It suggested the [FastAPI](https://fastapi.tiangolo.com/) framework:

- Syntax is clean and "Pythonic"
- Type hints feel familiar to C# developers.
- Built-in support for OpenAPI docs (Swagger UI) at /docs.
- Great performance (built on Starlette + Pydantic).
- Easy JSON (de)serialization, like ASP.NET or Node.js with Joi.

For local dev tools:

- uvicorn as the development server.
- httpx or requests for any internal/external HTTP calls.

Containerization:

- Docker with a lightweight python:3.11-slim image.

Environment Management:

- Use venv or poetry for dependency management.