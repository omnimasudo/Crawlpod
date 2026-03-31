"""
Module: data_processor.py
Description: Handles data processing tasks for the system.
"""

import numpy as np
from typing import List, Dict

def normalize_data(data: List[float]) -> List[float]:
    min_val = min(data)
    max_val = max(data)
    if max_val - min_val == 0:
        return [0.0 for _ in data]
    return [(x - min_val) / (max_val - min_val) for x in data]

def aggregate_data(records: List[Dict[str, float]]) -> Dict[str, float]:
    result = {}
    for key in records[0].keys():
        result[key] = sum(r[key] for r in records) / len(records)
    return result

def filter_outliers(data: List[float], threshold: float = 2.0) -> List[float]:
    mean = np.mean(data)
    std = np.std(data)
    return [x for x in data if abs(x - mean) <= threshold * std]

class DataProcessor:
    def __init__(self, data: List[float]):
        self.data = data

    def process(self) -> List[float]:
        filtered = filter_outliers(self.data)
        return normalize_data(filtered)
