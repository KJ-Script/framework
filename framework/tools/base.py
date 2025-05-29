"""
Base tool interface that defines the contract for all tool implementations.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseTool(ABC):
    """Base class for tool implementations."""
    
    @abstractmethod
    async def execute(self, page: Any, **kwargs) -> Any:
        """Execute the tool's functionality."""
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Get the tool's name."""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """Get the tool's description."""
        pass 