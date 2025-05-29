"""
Navigation tool for browser page navigation.
"""
from typing import Any, Dict
from .base import BaseTool

class NavigationTool(BaseTool):
    """Tool for handling page navigation."""
    
    @property
    def name(self) -> str:
        return "navigation"
    
    @property
    def description(self) -> str:
        return "Navigate to URLs and handle page loading"
    
    async def execute(self, page: Any, url: str, **kwargs) -> Any:
        """Navigate to the specified URL."""
        await page.goto(url)
        return {"status": "success", "url": url} 