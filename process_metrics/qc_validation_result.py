class QcValidationResult:
    def __init__(self, value: str, passed_qc: bool):
        self.value = value
        self.passed_qc = passed_qc
