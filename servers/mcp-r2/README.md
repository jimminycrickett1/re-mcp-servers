# mcp-r2

This directory contains the MCP server implementation for radare2 static analysis. The server wraps radare2 using r2pipe and exposes a set of deterministic tools via FastMCP.

## Tools

- `list_functions`: Return a dictionary describing functions discovered in the binary (name, start address, etc.).
- `list_strings`: Return a dictionary of ASCII/UTF-8 strings found in the binary.
- `disassemble`: Return disassembly instructions at the given address for a specified length.

## Status

This server is currently a stub. The method implementations need to be completed using r2pipe to interact with radare2 and extract meaningful analysis results. Contributions welcome!
