"""Shared test fixtures for codesteward-mcp tests."""


import pytest
from codesteward.mcp.config import McpConfig


@pytest.fixture
def cfg() -> McpConfig:
    """Minimal McpConfig with no Neo4j (stub mode)."""
    return McpConfig(
        neo4j_password="",  # triggers stub mode
        workspace_base="/tmp/codesteward-test-workspace",
        default_tenant_id="test-tenant",
        default_repo_id="test-repo",
    )


@pytest.fixture
def cfg_with_neo4j() -> McpConfig:
    """McpConfig that claims Neo4j is configured (password present).

    Note: does not actually connect — tests using this fixture must mock
    the neo4j driver.
    """
    return McpConfig(
        neo4j_uri="bolt://localhost:7687",
        neo4j_user="neo4j",
        neo4j_password="test-password",
        workspace_base="/tmp/codesteward-test-workspace",
        default_tenant_id="test-tenant",
        default_repo_id="test-repo",
    )
