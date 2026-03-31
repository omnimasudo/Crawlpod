"""
power_monitor.py
Monitors battery and power consumption.
"""

import random

class PowerMonitor:
    def __init__(self):
        self.voltage = 12.0
        self.current = 0.0

    def read_voltage(self) -> float:
        self.voltage = round(random.uniform(11.0, 12.6), 2)
        return self.voltage

    def read_current(self) -> float:
        self.current = round(random.uniform(0.5, 2.0), 2)
        return self.current

    def is_low_battery(self) -> bool:
        return self.voltage < 11.2
