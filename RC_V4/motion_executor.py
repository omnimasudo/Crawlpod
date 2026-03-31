"""
motion_executor.py
Executes planned motions and synchronizes leg movements.
"""

from typing import List

class MotionExecutor:
    def __init__(self, leg_controllers: List):
        self.leg_controllers = leg_controllers

    def execute_gait(self, gait_sequence: List[List[int]], steps: int = 1) -> None:
        for _ in range(steps):
            for group in gait_sequence:
                for leg_id in group:
                    self.leg_controllers[leg_id-1].move_to(1.0, 1.0, 1.0)

    def stop(self) -> None:
        for controller in self.leg_controllers:
            controller.calibrate()
