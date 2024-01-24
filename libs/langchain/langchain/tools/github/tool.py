"""
This tool allows agents to interact with the pygithub library
and operate on a GitHub repository.

To use this tool, you must first set as environment variables:
    GITHUB_API_TOKEN
    GITHUB_REPOSITORY -> format: {owner}/{repo}

"""
from typing import Optional
import logging

from langchain_core.pydantic_v1 import Field

from langchain.callbacks.manager import CallbackManagerForToolRun
from langchain.tools.base import BaseTool
from langchain.utilities.github import GitHubAPIWrapper


class GitHubAction(BaseTool):
    """Tool for interacting with the GitHub API.\n\n    To use this tool, you must first set the following environment variables:\n        - GITHUB_API_TOKEN\n        - GITHUB_REPOSITORY -> format: {owner}/{repo}\n\n    These environment variables are required to interact with the GitHub API and must be set before running the GitHub Actions workflow.\n"""

    api_wrapper: GitHubAPIWrapper = Field(default_factory=GitHubAPIWrapper)
    mode: str
    name: str = ""
    description: str = ""

    def _run(
        self,
        instructions: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the GitHub API to run an operation."""
        try:
            result = self.api_wrapper.run(self.mode, instructions)
            return result
        except Exception as e:
            logging.exception("An error occurred")
