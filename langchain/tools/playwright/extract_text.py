from __future__ import annotations

from typing import Type

from pydantic import BaseModel, root_validator

from langchain.tools.playwright.base import BaseBrowserTool
from langchain.tools.playwright.utils import aget_current_page, get_current_page


class ExtractTextTool(BaseBrowserTool):
    name: str = "extract_text"
    description: str = "Extract all the text on the current webpage"
    args_schema: Type[BaseModel] = BaseModel

    @root_validator
    def check_acheck_bs_importrgs(cls, values: dict) -> dict:
        """Check that the arguments are valid."""
        try:
            from bs4 import BeautifulSoup  # noqa: F401
        except ImportError:
            raise ValueError(
                "The 'beautifulsoup4' package is required to use this tool."
                " Please install it with 'pip install beautifulsoup4'."
            )
        return values

    def _run(self) -> str:
        """Use the tool."""
        # Use Beautiful Soup since it's faster than looping through the elements
        from bs4 import BeautifulSoup

        if self.sync_browser is None:
            raise ValueError(f"Synchronous browser not provided to {self.name}")

        page = get_current_page(self.sync_browser)
        html_content = page.content()

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, "lxml")

        return " ".join(soup.stripped_strings)

    async def _arun(self) -> str:
        """Use the tool."""
        if self.async_browser is None:
            raise ValueError(f"Asynchronous browser not provided to {self.name}")
        # Use Beautiful Soup since it's faster than looping through the elements
        from bs4 import BeautifulSoup

        page = await aget_current_page(self.async_browser)
        html_content = await page.content()

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, "lxml")

        return " ".join(soup.stripped_strings)
