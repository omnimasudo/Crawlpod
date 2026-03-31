"""
path_follower.py
Calculates and follows a path for navigation.
"""

from typing import List, Tuple

class PathFollower:
    def __init__(self):
        self.path: List[Tuple[float, float]] = []
        self.current_index = 0

    def set_path(self, path: List[Tuple[float, float]]) -> None:
        self.path = path
        self.current_index = 0

    def next_point(self) -> Tuple[float, float]:
        if self.current_index < len(self.path):
            point = self.path[self.current_index]
            self.current_index += 1
            return point
        return (0.0, 0.0)

    def has_more(self) -> bool:
        return self.current_index < len(self.path)
