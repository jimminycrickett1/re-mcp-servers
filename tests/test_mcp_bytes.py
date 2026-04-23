"""Minimal test suite for the mcp-bytes server.

These tests verify that the placeholder endpoints on the mcp-bytes
FastAPI app return a 200 response and the expected JSON keys. Hermes
and Overstory can extend these tests as the server gains real
functionality.
"""

from fastapi.testclient import TestClient
from servers.mcp_bytes.mcp_bytes_server import app

client = TestClient(app)


def test_read_bytes():
    """Basic sanity check for the /read_bytes endpoint."""
    response = client.get("/read_bytes", params={"start": 0, "length": 1})
    assert response.status_code == 200
    data = response.json()
    assert data.get("start") == 0
    assert data.get("length") == 1


def test_search_bytes():
    """Basic sanity check for the /search_bytes endpoint."""
    response = client.get("/search_bytes", params={"pattern": "deadbeef"})
    assert response.status_code == 200
    data = response.json()
    assert "matches" in data
