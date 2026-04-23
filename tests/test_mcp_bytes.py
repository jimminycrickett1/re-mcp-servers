import pytest
from servers.mcp_bytes.mcp_bytes_server import MCPBytesServer


def test_read_bytes():
    server = MCPBytesServer()
    data = b"\x00\x01\x02\x03\x04\x05"
    result = server.read_bytes(binary=data, offset=1, length=3)
    # read_bytes returns a dictionary with a hex string of the bytes
    assert result["bytes"] == data[1:4].hex()


def test_search_bytes():
    server = MCPBytesServer()
    data = b"\x00\x01\x00\x01\x00"
    # search for the pattern 0x00 in hex string format
    result = server.search_bytes(binary=data, pattern="00")
    # Expect offsets at positions 0, 2 and 4
    assert result["offsets"] == [0, 2, 4]
