from .metric import Metric
from .freemix import Freemix

from typing import List, Mapping, Optional

class AvailableMetrics:
    def __init__(self) -> None:
        self.metrics: List[Metric] = [
                Freemix()
        ]

        self.metrics_by_name: Mapping[str, Metric] = {}

        for m in self.metrics:
            self.metrics_by_name[m.name()] = m

    def metric_for_name(self, name: str) -> Optional[Metric]:
        return self.metrics_by_name.get(name)
