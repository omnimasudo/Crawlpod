"""
state_machine.py
Manages robot operational states and transitions.
"""

from typing import Callable, Dict

class StateMachine:
    def __init__(self):
        self.states: Dict[str, Callable] = {}
        self.current_state = None

    def add_state(self, name: str, handler: Callable) -> None:
        self.states[name] = handler

    def set_state(self, name: str) -> None:
        if name in self.states:
            self.current_state = name
        else:
            raise ValueError("Unknown state.")

    def run(self) -> None:
        if self.current_state and self.current_state in self.states:
            self.states[self.current_state]()
