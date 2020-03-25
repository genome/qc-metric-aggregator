from .metrics import Metric
from .qc_validation_result import QcValidationResult

from typing import Any, Callable, Mapping, Optional

class QcValidator:
    def __init__(self, metrics_dir: str) -> None:
        self.metrics_dir = metrics_dir

        self.evaluators: Mapping[str, Callable[[Any, Any], bool]] = {
                '<': lambda v, t : float(v) < float(t),
                '<=': lambda v, t : float(v) <= float(t),
                '>': lambda v, t : float(v) > float(t),
                '>=': lambda v, t : float(v) >= float(t),
                '=': lambda v, t : v == t,
                'report': lambda v, t: True
        }

    def validate(self, m: Metric, operation: str, threshold: Optional[str]) -> QcValidationResult:
        comparison_function = self.evaluators.get(operation)

        if comparison_function:
            metric_value = m.value(self.metrics_dir)
            passed_qc = comparison_function(metric_value, threshold)
            return QcValidationResult(str(metric_value), passed_qc)
        else:
            raise Exception(f"The specified operation {operation} was invalid. Only {str.join(',', self.evaluators.keys())} allowed.")
