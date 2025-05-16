from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class BaseProvider(ABC):
    
    def __init__(self, api_key: str, base_url: str):
        pass

    def generate_text(self, prompt: str, **kwargs) -> str:
        pass
    
    
