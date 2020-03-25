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
    requiredNamed = parser.add_argument_group('named arguments')
    requiredNamed.add_argument('-o', '--output-path', help='File path to store the finalized mertrics TSV', required=True)
    requiredNamed.add_argument('-t', '--threshold-file', help='Path to the yml thresholds file to validate against', required=True)
    args = parser.parse_args()

    if not os.path.isdir(args.output_path):
        raise Exception(f"{args.output_path} must be a directory.")

    if not os.path.isfile(args.threshold_file):
        raise Exception(f"{args.output_path} must be an existing file.")

    thresholds = ThresholdFileParser(args.threshold_file).thresholds()
    validator = QcValidator(args.metrics_dir)
    available_metrics = AvailableMetrics(args.sample_name)

    gen = ReportGenerator(args.sample_name, thresholds, available_metrics, validator)
    gen.generate_report(args.output_path)

    return

if __name__ == '__main__':
    generate_report()
