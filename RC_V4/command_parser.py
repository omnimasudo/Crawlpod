"""
command_parser.py
Parses and validates incoming control commands.
"""

from typing import Dict, Any

class CommandParser:
    def __init__(self):
        self.last_command = None

    def parse(self, command: str) -> Dict[str, Any]:
        parts = command.strip().split()
        if not parts:
            return {}
        cmd = parts[0].lower()
        args = parts[1:]
        self.last_command = cmd
        return {'command': cmd, 'args': args}

    def is_valid(self, command: str) -> bool:
        return bool(command and command.strip())
