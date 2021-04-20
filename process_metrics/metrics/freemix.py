from .metric import Metric
from .tsv_metric import TSVMetric

class Freemix(Metric[float], TSVMetric):

    def value(self, metrics_dir: str) -> float:
        value = self.extract_metric(metrics_dir)
        return float(value)

    def name(self) -> str:
        return 'FREEMIX'

    def metric_column_name(self) -> str:
        return self.name()

    def metric_file_pattern(self) -> str:
        return rf".+/{self.sample_id}\.verify_bam_id\..+"

    def skip_commented_lines(self) -> bool:
        return False

