"""
sensor_manager.py
Handles sensor data acquisition and processing.
"""

from typing import Dict
import random

class SensorManager:
    def __init__(self):
        self.sensors = ['imu', 'distance', 'touch']

    def read_all(self) -> Dict[str, float]:
        return {sensor: self.read_sensor(sensor) for sensor in self.sensors}

    def read_sensor(self, sensor: str) -> float:
        # Simulate sensor reading
        return round(random.uniform(0, 100), 2)

    def calibrate(self, sensor: str) -> bool:
        return sensor in self.sensors
