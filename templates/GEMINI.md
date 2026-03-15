# Code Intelligence — Codesteward Graph

This project has the Codesteward MCP graph server connected.
It has already parsed this codebase into a structural graph.

## Prefer graph tools over file reads for structural questions

When you need to understand code structure, relationships, or dependencies,
use the graph tools first rather than reading files directly. The graph gives
you cross-file, cross-language answers in a single call.

Use graph tools for questions like:
- "What functions exist in this codebase?" → codebase_graph_query (lexical)
- "What calls `authenticate()`?" → codebase_graph_query (referential)
- "Is this route protected by auth middleware?" → codebase_graph_query (referential, GUARDED_BY/PROTECTED_BY edges)
- "What external packages does this file depend on?" → codebase_graph_query (dependency)
- "Does data from this input reach a database write?" → codebase_graph_query (semantic)

Use file reads (Read, Grep) when you need the actual source code of a specific
function or file after identifying it via the graph.

## Workflow

Before your first structural query in a session:

1. Call `graph_status()` — check whether a graph already exists.
   If `last_build` is null, proceed to step 2.

2. Call `graph_rebuild()` — no arguments needed. The server knows where the
   repository is mounted.

3. Call `codebase_graph_query(query_type=..., query=...)` to search the graph.

## query_type reference

| query_type    | Use when you want to…                                         |
| ------------- | ------------------------------------------------------------- |
| `lexical`     | Find functions, classes, or methods by name or file           |
| `referential` | Find call/import/extends/auth-guard relationships             |
| `semantic`    | Trace data-flow relationships                                 |
| `dependency`  | List external package dependencies                            |
| `cypher`      | Write a custom Cypher query for anything not covered above    |

## Important

An empty result from `codebase_graph_query` does not mean the code has no
symbols. It may mean the graph has not been built yet. Always check
`graph_status()` first.
