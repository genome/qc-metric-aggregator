from typing import List, Tuple

import os.path

from .metric_threshold import MetricThreshold
from .qc_validator import QcValidator
from .metrics import AvailableMetrics

class ReportGenerator:
    def __init__(self, sample_id: str, thresholds: List[MetricThreshold], available_metrics: AvailableMetrics, validator: QcValidator) -> None:
        self.sample_id = sample_id
        self.thresholds = thresholds
        self.available_metrics = available_metrics
        self.validator = validator

    def generate_report(self, output_path) -> None:
        data = self.gather_metrics()
        headers = data[0]
        values = data[1]
        with open(output_path, 'w') as fout:
            print(str.join("\t", headers), file=fout)
            print(str.join("\t", values), file=fout)


    def gather_metrics(self) -> Tuple[List[str], List[str]]:
        headers: List[str] = ['sample_id', 'qc_status']
        values: List[str] = []
        pass_fail_results: List[bool] = []
        qc_status = ''

        for t in self.thresholds:
            metric = self.available_metrics.metric_for_name(t.metric_name)
            if not metric:
                raise Exception(f"No registered metric matches name {t.metric_name}.")
            else:
                headers.append(metric.name())
                res = self.validator.validate(metric, t.operator, t.value)
                pass_fail_results.append(res.passed_qc)
                values.append(res.value)

        if all(pass_fail_results):
            qc_status = 'PASS'
        else:
            qc_status = 'FAIL'

        final_values = [self.sample_id, qc_status] + values

        return (headers, final_values)

