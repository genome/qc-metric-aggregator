import yaml

from typing import List

from .metric_threshold import MetricThreshold

class ThresholdFileParser:
    def __init__(self, threshold_file) -> None:
        with open(threshold_file) as f:
            self.file_contents = yaml.safe_load(f)

    def thresholds(self) -> List[MetricThreshold]:
        metric_thresholds: List[MetricThreshold] = []

        for t in self.file_contents:
            if 'metric_name' not in t:
                raise Exception(f"metric_name is required for a threshold")
            if 'operator' not in t:
                raise Exception(f"operator is required for a threshold")
            if 'value' not in t and t['operator'] != 'report':
                raise Exception(f"value is required for a threshold")

            metric_thresholds.append(
                MetricThreshold(t['metric_name'], t.get('value'), t['operator'])
            )

        return metric_thresholds

