"""
gait_planner.py
Plans and generates gait sequences for hexapod movement.
"""

from typing import List, Dict

class GaitPlanner:
    def __init__(self):
        self.gaits = {
            'tripod': [[1,4,5],[2,3,6]],
            'wave': [[1],[2],[3],[4],[5],[6]],
        }
        self.current_gait = 'tripod'

    def set_gait(self, gait_name: str) -> None:
        if gait_name in self.gaits:
            self.current_gait = gait_name
        else:
            raise ValueError("Unknown gait type.")

    def get_gait_sequence(self) -> List[List[int]]:
        return self.gaits[self.current_gait]

    def add_gait(self, name: str, sequence: List[List[int]]) -> None:
        self.gaits[name] = sequence
