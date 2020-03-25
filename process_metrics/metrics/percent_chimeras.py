from collections import OrderedDict

from .metric import Metric
from .tsv_metric import TSVMetric

class PercentChimeras(Metric[float], TSVMetric):

    def value(self, metrics_dir: str) -> float:
        value = self.extract_metric(metrics_dir)
        return float(value)

    def name(self) -> str:
        return 'PCT_CHIMERAS'

    def metric_column_name(self) -> str:
        return self.name()

    def metric_file_pattern(self) -> str:
        return rf".+{self.sample_id}\.alignment_summary_metrics"

    def custom_filter(self, row: OrderedDict[str,str]) -> bool:
        return row['CATEGORY'] == 'PAIR'

