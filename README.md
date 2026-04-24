# re-mcp-servers

## Running mcp-bytes

The `mcp-bytes` server is a FastAPI application that exposes basic
byte-level operations. To run the server locally:

1. Install dependencies. You can use [Poetry](https://python-poetry.org/) if
   you have it installed:

   ```bash
   poetry install
   ```

   Alternatively, install in editable mode with pip:

   ```bash
   pip install -e .
   ```

2. Launch the server with Uvicorn:

   ```bash
   uvicorn servers.mcp_bytes.mcp_bytes_server:app --reload
   ```

   The `--reload` flag enables auto-reload during development. The server
   will listen on `http://127.0.0.1:8000/`. You can interact with the API
   via your browser or using `curl`.

## Running tests

Tests live under the `tests` directory and use [pytest](https://docs.pytest.org/).
To run them:

```bash
pytest
```

Tests help ensure your implementations behave deterministically and return
the expected fields. Hermes/Overstory will use these tests as part of
its iterative development loop.

## Running the MCP-bytes server

Install dependencies and run via uvicorn:

```
pip install fastapi fastmcp uvicorn
uvicorn servers.mcp_bytes.mcp_bytes_server:app --reload
```

This exposes `/read_bytes` and `/search_bytes` endpoints.
