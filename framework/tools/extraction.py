"""
Extraction tool for getting data from web pages.
"""
from typing import Any, Dict, List
from .base import BaseTool

class ExtractionTool(BaseTool):
    """Tool for extracting data from web pages."""
    
    @property
    def name(self) -> str:
        return "extraction"
    
    @property
    def description(self) -> str:
        return "Extract data from web pages using selectors"
    
    async def execute(self, page: Any, selector: str, **kwargs) -> Any:
        """Extract data using the specified selector."""
        elements = await page.query_selector_all(selector)
        results = []
        for element in elements:
            text = await element.text_content()
            results.append(text.strip())
        return results 