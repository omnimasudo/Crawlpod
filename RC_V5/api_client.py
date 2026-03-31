"""
Module: api_client.py
Description: Handles API requests and responses.
"""

import requests
from typing import Any, Dict

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, endpoint: str, params: Dict[str, Any] = None) -> Any:
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        return None

    def post(self, endpoint: str, data: Dict[str, Any]) -> Any:
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        return None
