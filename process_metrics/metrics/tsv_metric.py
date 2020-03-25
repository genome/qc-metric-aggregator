import re
import csv
import glob
import os.path

from abc import ABC, abstractmethod

class TSVMetric:

    @abstractmethod
    def metric_file_pattern(self) -> str:
        pass

    @abstractmethod
    def metric_column_name(self) -> str:
        pass

    def extract_metric(self, metrics_dir: str) -> str:
        metrics_file = self.identify_metrics_file(metrics_dir)
        return self.read_metric(metrics_file)

    def delimiter(self) -> str:
        return "\t"

    def identify_metrics_file(self, metrics_dir: str) -> str:
        regex = re.compile(
                    self.metric_file_pattern(),
                    re.IGNORECASE)

        glob_path = os.path.join(metrics_dir, '**')
        all_files = glob.glob(glob_path, recursive = True)

        candidate_files =  [f for f in all_files if regex.match(f)]

        if len(candidate_files) > 1:
            raise Exception(f"Ambiguous metrics file. Matcher {self.metric_file_pattern()} matches multiple files in {metrics_dir}.")
        if len(candidate_files) == 0:
            raise Exception(f"Metrics file not found. Matcher {self.metric_file_pattern()} matches no files in {metrics_dir}.")

        return candidate_files[0]

    def read_metric(self, filename: str) -> str:
        values = []
        with open(filename) as file:
            reader = csv.DictReader(file, delimiter=self.delimiter())
            for row in reader:
                values.append(row[self.metric_column_name()])

        if len(values) > 1:
            raise Exception(f"Ambiguous metric value. Found {len(values)} values for {self.metric_column_name()}.")
        if len(values) == 0:
            raise Exception(f"Missing metric value. Found {len(values)} values for {self.metric_column_name()}.")

        return values[0]
