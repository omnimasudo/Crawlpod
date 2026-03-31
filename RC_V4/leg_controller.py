"""
leg_controller.py
Controls individual leg kinematics and servo positions.
"""

from typing import List

class LegController:
    def __init__(self, leg_id: int):
        self.leg_id = leg_id
        self.joint_angles = [0.0, 0.0, 0.0]

    def set_joint_angles(self, angles: List[float]) -> None:
        if len(angles) != 3:
            raise ValueError("Each leg must have 3 joint angles.")
        self.joint_angles = angles

    def get_joint_angles(self) -> List[float]:
        return list(self.joint_angles)

    def move_to(self, x: float, y: float, z: float) -> None:
        # Placeholder for inverse kinematics
        self.joint_angles = [x, y, z]

    def calibrate(self) -> None:
        self.joint_angles = [0.0, 0.0, 0.0]
