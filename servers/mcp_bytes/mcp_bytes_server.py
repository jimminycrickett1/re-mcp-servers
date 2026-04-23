"""Skeleton FastMCP server exposing basic byte-level operations.

This initial implementation is intentionally minimal. It defines a FastAPI app
with placeholders for byte-oriented operations such as reading ranges and
searching for patterns. Hermes/Overstory can iterate on this skeleton to
implement the actual logic.
"""

from fastapi import FastAPI, HTTPException

app = FastAPI(title="mcp-bytes", version="0.1.0")


@app.get("/read_bytes")
async def read_bytes(start: int, length: int):
    """Read a range of bytes from a file (placeholder).

    Args:
        start: The starting offset.
        length: Number of bytes to read.
    Returns:
        A JSON object with a placeholder response.
    """
    # TODO: replace with actual implementation that reads from an artifact
    if start < 0 or length <= 0:
        raise HTTPException(status_code=400, detail="Invalid parameters")
    return {"data": "", "start": start, "length": length}


@app.get("/search_bytes")
async def search_bytes(pattern: str):
    """Search for a byte pattern in a file (placeholder).

    Args:
        pattern: A hex-encoded search pattern.
    Returns:
        A list of offsets where the pattern occurs (empty by default).
    """
    # TODO: replace with actual implementation
    return {"matches": []}
