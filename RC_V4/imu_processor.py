"""
imu_processor.py
Processes IMU (Inertial Measurement Unit) data for orientation.
"""

from typing import Dict
import math

class IMUProcessor:
    def __init__(self):
        self.orientation = {'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0}

    def update(self, imu_data: Dict[str, float]) -> None:
        self.orientation['roll'] = imu_data.get('roll', 0.0)
        self.orientation['pitch'] = imu_data.get('pitch', 0.0)
        self.orientation['yaw'] = imu_data.get('yaw', 0.0)

    def get_orientation(self) -> Dict[str, float]:
        return dict(self.orientation)

    def is_stable(self, threshold: float = 5.0) -> bool:
        return all(abs(v) < threshold for v in self.orientation.values())
