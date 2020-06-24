from .metric import Metric
from .tsv_metric import TSVMetric

class MeanTargetCoverage(Metric[float], TSVMetric):

    def value(self, metrics_dir: str) -> float:
        value = self.extract_metric(metrics_dir)
        return float(value)

    def name(self) -> str:
        return 'MEAN_TARGET_COVERAGE'

    def metric_column_name(self) -> str:
        return self.name()

    def metric_file_pattern(self) -> str:
        return rf".+{self.sample_id}\.hs_metrics"

    def take_first_value(self) -> bool:
        return True
