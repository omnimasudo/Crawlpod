"""
Module: user_profile.py
Description: Manages user profile data and operations.
"""

from typing import Dict

class UserProfile:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.attributes: Dict[str, str] = {}

    def update_email(self, new_email: str):
        self.email = new_email

    def set_attribute(self, key: str, value: str):
        self.attributes[key] = value

    def get_attribute(self, key: str) -> str:
        return self.attributes.get(key, "")

    def to_dict(self) -> Dict[str, str]:
        return {"username": self.username, "email": self.email, **self.attributes}
