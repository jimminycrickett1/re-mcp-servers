"""MCP server for raw byte operations.

This module defines a minimal MCP server exposing deterministic byte-level operations. It uses the `fastmcp` library to
declare tools that can be consumed by agent clients such as Hermes.

The implementation here is deliberately simple and does not read from the filesystem. Instead, it assumes the caller
will supply the binary data as a `bytes` parameter. Real deployments may wrap these calls around a persistence layer
that maps artifact identifiers to concrete byte arrays.
"""

from typing import Dict, List

from fastmcp import tool  # type: ignore
from fastmcp.server import Server  # type: ignore


class MCPBytesServer(Server):
    """A minimal MCP server for byte-level operations."""

    def __init__(self) -> None:
        super().__init__()

    @tool(description="Read a slice of bytes from an in-memory binary.")
    def read_bytes(self, binary: bytes, offset: int, length: int) -> bytes:
        """Return a slice of `length` bytes starting at `offset`."""
        return binary[offset : offset + length]

    @tool(description="Search for a pattern in an in-memory binary.")
    def search_bytes(self, binary: bytes, pattern: bytes) -> Dict[str, List[int]]:
        """Return all offsets where `pattern` occurs in `binary`."""
        offsets: List[int] = []
        start = 0
        while True:
            idx = binary.find(pattern, start)
            if idx < 0:
                break
            offsets.append(idx)
            start = idx + 1
        return {"offsets": offsets}
