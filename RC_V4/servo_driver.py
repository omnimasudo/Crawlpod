"""
servo_driver.py
Low-level interface for controlling servo motors.
"""

from typing import List

class ServoDriver:
    def __init__(self, num_servos: int):
        self.num_servos = num_servos
        self.positions = [0.0] * num_servos

    def set_position(self, servo_id: int, angle: float) -> None:
        if 0 <= servo_id < self.num_servos:
            self.positions[servo_id] = angle

    def get_position(self, servo_id: int) -> float:
        return self.positions[servo_id]

    def reset_all(self) -> None:
        self.positions = [0.0] * self.num_servos
