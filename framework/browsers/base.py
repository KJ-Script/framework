"""
Base browser interface that defines the contract for all browser implementations.
"""
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

class BaseBrowser(ABC):
    """Base class for browser implementations."""
    
    @abstractmethod
    async def initialize(self, headless: bool = True, **kwargs) -> None:
        """Initialize the browser with given configuration."""
        pass
    
    @abstractmethod
    async def new_page(self) -> Any:
        """Create a new browser page."""
        pass
    
    @abstractmethod
    async def close(self) -> None:
        """Close the browser and cleanup resources."""
        pass
    
    @abstractmethod
    async def set_viewport(self, width: int, height: int) -> None:
        """Set the browser viewport size."""
        pass 