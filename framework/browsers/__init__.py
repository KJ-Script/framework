"""
Browser management package for the framework.
Handles browser initialization, session management, and browser state control.
"""

from .base import BaseBrowser
from .playwright import PlaywrightBrowser

__all__ = ['BaseBrowser', 'PlaywrightBrowser'] 