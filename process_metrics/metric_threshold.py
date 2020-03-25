from typing import Optional

class MetricThreshold:
    def __init__(self, metric_name: str, value: Optional[str], operator: str):
        self.metric_name = metric_name
        self.value = value
        self.operator = operator
