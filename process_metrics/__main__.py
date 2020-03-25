import argparse
import os.path

from .threshold_file_parser import ThresholdFileParser
from .qc_validator import QcValidator
from .metrics import AvailableMetrics
from .report_generator import ReportGenerator

def generate_report() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('sample_name', help='The sample name or id for which the QC metrics apply')
    parser.add_argument('metrics_dir', help='The directory to search for metric files, often a cromwell run directory')
    parser.add_argument('output_file', help='File path to store the finalized mertrics TSV')
    parser.add_argument('threshold_file', help='Path to the yml thresholds file to validate against')
    args = parser.parse_args()

    if not os.path.isfile(args.threshold_file):
        raise Exception(f"{args.threshold_file} must be an existing file.")

    if not os.path.isdir(os.path.join(args.metrics_dir, '')):
        raise Exception(f"{args.metrics_dir} must be a directory.")

    thresholds = ThresholdFileParser(args.threshold_file).thresholds()
    validator = QcValidator(args.metrics_dir)
    available_metrics = AvailableMetrics(args.sample_name)

    gen = ReportGenerator(args.sample_name, thresholds, available_metrics, validator)
    gen.generate_report(args.output_file)

    return

if __name__ == '__main__':
    generate_report()
