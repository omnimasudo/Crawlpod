"""
Module: report_generator.py
Description: Generates reports from system data.
"""

from typing import List, Dict
import datetime

class ReportGenerator:
    def __init__(self, data: List[Dict[str, float]]):
        self.data = data

    def generate_summary(self) -> Dict[str, float]:
        summary = {}
        for key in self.data[0].keys():
            summary[key] = sum(d[key] for d in self.data) / len(self.data)
        return summary

    def export_csv(self, path: str) -> bool:
        try:
            with open(path, 'w') as f:
                headers = ','.join(self.data[0].keys())
                f.write(headers + '\n')
                for row in self.data:
                    f.write(','.join(str(row[k]) for k in row.keys()) + '\n')
            return True
        except Exception:
            return False

    def timestamp(self) -> str:
        return datetime.datetime.now().isoformat()
