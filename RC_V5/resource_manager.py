"""
Module: resource_manager.py
Description: Manages system resources and allocation.
"""

from typing import Dict

class ResourceManager:
    def __init__(self):
        self.resources: Dict[str, int] = {}

    def allocate(self, name: str, amount: int) -> bool:
        if self.resources.get(name, 0) + amount < 0:
            return False
        self.resources[name] = self.resources.get(name, 0) + amount
        return True

    def release(self, name: str, amount: int) -> bool:
        if self.resources.get(name, 0) < amount:
            return False
        self.resources[name] -= amount
        return True

    def get_status(self) -> Dict[str, int]:
        return self.resources.copy()
