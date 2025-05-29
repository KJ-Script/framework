"""
Simple in-memory storage utility.
"""
from typing import Any, Dict, Optional

class Memory:
    """Simple in-memory storage for agent state."""
    
    def __init__(self):
        self._storage: Dict[str, Any] = {}
    
    def set(self, key: str, value: Any) -> None:
        """Set a value in memory."""
        self._storage[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a value from memory."""
        return self._storage.get(key, default)
    
    def clear(self) -> None:
        """Clear all stored values."""
        self._storage.clear()
    
    def update(self, data: Dict[str, Any]) -> None:
        """Update multiple values at once."""
        self._storage.update(data) 