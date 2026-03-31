"""
Module: auth_manager.py
Description: Manages authentication and user sessions.
"""

import hashlib
import uuid
from typing import Dict

class AuthManager:
    def __init__(self):
        self.sessions: Dict[str, str] = {}
        self.users: Dict[str, str] = {}

    def register_user(self, username: str, password: str) -> bool:
        if username in self.users:
            return False
        self.users[username] = self._hash_password(password)
        return True

    def login(self, username: str, password: str) -> str:
        if username not in self.users:
            return ""
        if self.users[username] != self._hash_password(password):
            return ""
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = username
        return session_id

    def logout(self, session_id: str) -> bool:
        return self.sessions.pop(session_id, None) is not None

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
