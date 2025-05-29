"""
Base agent interface that defines the contract for all agent implementations.
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from ..browsers import BaseBrowser
from ..tools import BaseTool

class BaseAgent(ABC):
    """Base class for agent implementations."""
    
    def __init__(self, browser: BaseBrowser, tools: List[BaseTool], task: str):
        self.browser = browser
        self.tools = tools
        self.task = task
        self.memory: Dict[str, Any] = {}
    
    @abstractmethod
    async def run(self) -> None:
        """Run the agent's main execution loop."""
        pass
    
    @abstractmethod
    async def _decide_next_action(self) -> Dict[str, Any]:
        """Decide the next action to take based on current state."""
        pass
    
    @abstractmethod
    async def _execute_action(self, action: Dict[str, Any]) -> Any:
        """Execute the decided action."""
        pass 