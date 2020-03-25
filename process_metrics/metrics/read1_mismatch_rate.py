from typing import Dict

from .metric import Metric
from .tsv_metric import TSVMetric

class Read1MismatchRate(Metric[float], TSVMetric):

    def value(self, metrics_dir: str) -> float:
        value = self.extract_metric(metrics_dir)
        return float(value)

    def name(self) -> str:
        return 'READ1_PF_MISMATCH_RATE'

    def metric_column_name(self) -> str:
        return 'PF_MISMATCH_RATE'

    def metric_file_pattern(self) -> str:
        return rf".+{self.sample_id}\.alignment_summary_metrics"

    def custom_filter(self, row: Dict[str,str]) -> bool:
        return all([
            row['CATEGORY'] == 'FIRST_OF_PAIR',
            row['SAMPLE'].strip(),
            not row['READ_GROUP'],
            not row['LIBRARY'],
        ])

