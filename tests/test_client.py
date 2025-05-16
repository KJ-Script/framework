"""
Tests for the Framework client.
"""

import pytest
from framework import Client


def test_client_initialization():
    """Test client initialization."""
    client = Client()
    assert isinstance(client, Client)
    assert client.api_key is None


def test_client_with_api_key():
    """Test client initialization with API key."""
    api_key = "test_key"
    client = Client(api_key=api_key)
    assert client.api_key == api_key 