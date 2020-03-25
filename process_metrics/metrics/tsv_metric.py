import re
import csv
import glob
import os.path

from typing import Dict

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
            if self.skip_commented_lines():
                file_without_comments = filter(lambda row: row.strip() and not row.startswith('#'), file)
                reader = csv.DictReader(file_without_comments, delimiter=self.delimiter())
            else:
                reader = csv.DictReader(file, delimiter=self.delimiter())

            for row in reader:
                if self.custom_filter(row):
                    values.append(row[self.metric_column_name()])
                    if self.take_first_value():
                        break

        if len(values) > 1 and not self.take_first_value():
            raise Exception(f"Ambiguous metric value. Found {len(values)} values for {self.metric_column_name()}.")
        if len(values) == 0:
            raise Exception(f"Missing metric value. Found {len(values)} values for {self.metric_column_name()}.")

        return values[0]

    def skip_commented_lines(self) -> bool:
        return True

    def take_first_value(self) -> bool:
        return False

    def custom_filter(self, row: Dict[str,str]) -> bool:
        return True
