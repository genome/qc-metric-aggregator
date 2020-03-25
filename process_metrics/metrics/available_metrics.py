from .metric import Metric
from .freemix import Freemix
from .q20_bases import Q20Bases
from .mean_coverage import MeanCoverage
from .percent_10x import Percent10x
from .percent_20x import Percent20x
from .percent_chimeras import PercentChimeras
from .median_insert_size import MedianInsertSize

from typing import List, Mapping, Optional

class AvailableMetrics:
    def __init__(self, sample_id: str) -> None:
        self.metrics: List[Metric] = [
                Freemix(sample_id),
                Q20Bases(sample_id),
                MeanCoverage(sample_id),
                Percent10x(sample_id),
                Percent20x(sample_id),
                PercentChimeras(sample_id),
                MedianInsertSize(sample_id)
        ]

        self.metrics_by_name: Mapping[str, Metric] = {}

        for m in self.metrics:
            self.metrics_by_name[m.name()] = m

    def metric_for_name(self, name: str) -> Optional[Metric]:
        return self.metrics_by_name.get(name)
