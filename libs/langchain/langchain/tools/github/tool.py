"""
This tool allows agents to interact with the pygithub library
and operate on a GitHub repository.

To use this tool, you must first set as environment variables:
    GITHUB_API_TOKEN
    GITHUB_REPOSITORY -> format: {owner}/{repo}

"""
from typing import Optional

from langchain_core.pydantic_v1 import Field

from langchain.callbacks.manager import CallbackManagerForToolRun
from langchain.tools.base import BaseTool
from langchain.utilities.github import GitHubAPIWrapper


class GitHubAction(BaseTool):
    """Tool for interacting with the GitHub API."""

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
        # Add code to handle the specific error or issue causing the failure.\n        try:\n            result = self.api_wrapper.run(self.mode, instructions)\n            return result\n        except SpecificErrorType as e:\n            # Handle the error\n            return str(e)
