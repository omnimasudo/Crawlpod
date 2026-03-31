"""
Module: config_loader.py
Description: Loads and validates configuration files.
"""

import json
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, path: str):
        self.path = path
        self.config: Dict[str, Any] = {}

    def load(self) -> bool:
        try:
            with open(self.path, 'r') as f:
                self.config = json.load(f)
            return True
        except (IOError, json.JSONDecodeError):
            return False

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def validate(self, required_keys: list) -> bool:
        return all(key in self.config for key in required_keys)
