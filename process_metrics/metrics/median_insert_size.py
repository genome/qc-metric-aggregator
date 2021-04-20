from typing import Dict

from .metric import Metric
from .tsv_metric import TSVMetric

class MedianInsertSize(Metric[float], TSVMetric):

    def value(self, metrics_dir: str) -> float:
        value = self.extract_metric(metrics_dir)
        return float(value)

    def name(self) -> str:
        return 'MEDIAN_INSERT_SIZE'

    def metric_column_name(self) -> str:
        return self.name()

    def metric_file_pattern(self) -> str:
        return rf".+/{self.sample_id}\.insert_size_metrics"

    def take_first_value(self) -> bool:
        return True

    def custom_filter(self, row: Dict[str,str]) -> bool:
        return all([
            not row['READ_GROUP'],
            not row['LIBRARY'],
        ])
