# Changelog

All notable changes to `codesteward-graph` and `codesteward-mcp` are documented here.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

Both packages share a version number and are always released together.

---

## [Unreleased]

## [0.2.1] — 2026-03-15

### Fixed — codesteward-mcp

- Docker `CMD` was hardcoded to `--transport http`, overriding the `ENV TRANSPORT=sse` env var
  and causing the container to start on Streamable HTTP instead of SSE

## [0.2.0] — 2026-03-15

### Fixed — codesteward-graph

- `GraphEdge` model was missing `confidence` and `source` fields required by `graph_augment`
- Python parser: `is_async` flag not set for `async def` functions under tree-sitter-python ≥ 0.25
  (grammar now emits `function_definition` with an `async` child rather than `async_function_definition`)
- tree-sitter `Parser` initialisation updated to the ≥ 0.22 API (`Parser(language)` instead of
  `Parser().set_language(language)`)
- Optional-language test classes (Go, C, C++, Rust, PHP, C#, Kotlin, Scala) now skip gracefully
  with `pytest.importorskip` when the corresponding grammar package is not installed
- PyPI classifier corrected from `BSD Software License` to `BSD License`

### Fixed — codesteward-mcp

- Default transport switched from Streamable HTTP (`http`) to SSE (`sse`) so that Claude Code
  and other clients that do not send `Accept: text/event-stream` can connect without a 406 error
- SSE transport now served via `mcp.sse_app()` + uvicorn (consistent with the `http` branch)
- Docker image: `mkdir /workspace` moved before `USER codesteward` to avoid permission denied
- Health check replaced with a TCP socket probe (works on both SSE and HTTP transports)
- `TRANSPORT` environment variable default updated to `sse` in `Dockerfile.mcp` and
  `docker-compose.yml`
- CI and release workflows: `uv sync` now installs `--extra graph` so core grammar tests run
- All template `.mcp.json` / agent config files updated to point to `/sse` endpoint

### Changed — codesteward-mcp

- MCP endpoint URL changed from `http://localhost:3000/mcp` to `http://localhost:3000/sse`

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

[Unreleased]: https://github.com/bitkaio/codesteward/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/bitkaio/codesteward/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/bitkaio/codesteward/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/bitkaio/codesteward/releases/tag/v0.1.0
