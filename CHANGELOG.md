# Changelog

All notable changes to `codesteward-graph` and `codesteward-mcp` are documented here.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

Both packages share a version number and are always released together.

---

## [Unreleased]

## [0.1.0] — 2026-03-15

### Added — codesteward-graph

- Tree-sitter AST parsers for 13 languages: TypeScript, JavaScript (including TSX/JSX/MJS/CJS),
  Python, Java, Go, Rust, PHP, C#, Kotlin, Scala, C, C++
- Regex-based parser for COBOL (no tree-sitter grammar available)
- `CALLS` edge extraction with cross-file target resolution
- `IMPORTS`, `EXTENDS`, `DEPENDS_ON`, `DATA_FLOW` edge extraction
- `GUARDED_BY` edges for function-level auth guards: Python decorators, FastAPI `Depends`,
  TypeScript/Java annotations (`@UseGuards`, `@PreAuthorize`, etc.)
- `PROTECTED_BY` edges for router-scope auth guards: FastAPI `APIRouter(dependencies=[...])`,
  Express `router.use()`, Gin `group.Use()`, Actix `scope().wrap()`,
  Laravel `Route::middleware()->group()`, ASP.NET `MapGroup().RequireAuthorization()`
- SQL context tagging via template literal detection
- `GraphBuilder` with full and incremental parse modes
- Neo4j writer with tenant + repo namespacing; stub mode without Neo4j
- `PackageJsonParser` for `package.json` dependency extraction

### Added — codesteward-mcp

- MCP server over HTTP+SSE (Streamable HTTP, MCP 2025-03-26 spec) and stdio transports
- Four tools: `graph_rebuild`, `codebase_graph_query`, `graph_augment`, `graph_status`
- Five named query types: `lexical`, `referential`, `semantic`, `dependency`, `cypher`
- `McpConfig` via pydantic-settings — env vars, YAML file, or CLI flags
- `default_repo_path` — zero-argument `graph_rebuild` in the Docker setup
- Docker image and `docker-compose.yml` with Neo4j
- Templates for Claude Code, Cursor, Windsurf, VS Code, Gemini CLI, Continue.dev,
  Claude Desktop (`.mcp.json`, `.cursorrules`, `GEMINI.md`, `.windsurfrules`,
  `copilot-instructions.md`, `CLAUDE.md`)

[Unreleased]: https://github.com/bitkaio/codesteward-mcp/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/bitkaio/codesteward-mcp/releases/tag/v0.1.0
