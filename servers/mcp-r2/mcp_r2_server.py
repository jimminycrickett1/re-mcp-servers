"""MCP server skeleton for radare2-based static analysis.

This server is intended to wrap radare2 or rizin to expose basic static analysis primitives such as listing functions, imports, exports, strings and disassembly.

At this stage the implementation simply provides method stubs with descriptive docstrings. Real functionality should be implemented using Python bindings to radare2 (e.g. r2pipe).
"""

from fastmcp import tool  # type: ignore
from fastmcp.server import Server  # type: ignore
from typing import Dict, List, Any


class MCPR2Server(Server):
    """Stub MCP server for radare2 static analysis."""

    def __init__(self) -> None:
        super().__init__()

    @tool(description="List function symbols in a binary.")
    def list_functions(self, binary_path: str) -> Dict[str, Any]:
        """Return a dictionary describing functions discovered in the binary.

        This stub returns an empty dictionary. A real implementation should use
        r2pipe to analyze the binary and extract function symbols.
        """
        return {"functions": []}

    @tool(description="List strings in a binary.")
    def list_strings(self, binary_path: str) -> Dict[str, List[str]]:
        """Return a dictionary of ASCII/UTF-8 strings found in the binary.

        This stub returns an empty list. A real implementation should use r2pipe
        or an equivalent library to scan for strings.
        """
        return {"strings": []}

    @tool(description="Disassemble a function at the given address.")
    def disassemble(self, binary_path: str, address: int, length: int = 128) -> Dict[str, Any]:
        """Return a dictionary containing disassembly lines.

        This stub returns an empty list. A real implementation should use r2pipe
        to disassemble instructions at the given address.
        """
        return {"instructions": []}
