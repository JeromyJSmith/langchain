"""Integration test for Github Wrapper."""
import pytest
from unittest import mock

from langchain.utilities.github import GitHubAPIWrapper

# Make sure you have set the following env variables:
# GITHUB_REPOSITORY
# GITHUB_BRANCH
# GITHUB_APP_ID
# GITHUB_PRIVATE_KEY


@pytest.fixture
def api_client() -> GitHubAPIWrapper:
    return GitHubAPIWrapper()


def test_get_open_issues(api_client: GitHubAPIWrapper, mocker) -> None:
    """Basic test to fetch issues"""
    mocker.patch.object(GitHubAPIWrapper, 'get_issues', return_value=[{'title': 'Test Issue', 'number': 1}])
    issues = api_client.get_issues()
    assert len(issues) != 0
