# qc-metric-aggregator

[![Build Status](https://travis-ci.org/genome/qc-metric-aggregator.svg?branch=master)](https://travis-ci.org/genome/qc-metric-aggregator)

Parse individual metrics out of a directory of QC results for genomic data and output a report containing the desired metrics and the overall PASS/FAIL status of the sample.


#### Installation

------------

`pip install qc-metric-aggregator`

------------

#### Usage

------------

    usage: aggregate-qc-metrics [-h]
                                sample_name metrics_dir output_file threshold_file

    positional arguments:
      sample_name     The sample name or id for which the QC metrics apply
      metrics_dir     The directory to search for metric files, often a cromwell
                      run directory
      output_file     File path to store the finalized mertrics TSV
      threshold_file  Path to the yml thresholds file to validate against

    optional arguments:
      -h, --help      show this help message and exit


Example invocation:

    aggregate-qc-metrics HG00096 /opt/qc/results/HG00096/WholeGenomeSingleSampleQc /opt/qc/scores/qc_results.tsv thresholds.yml

------------
**Output formats**


Coming soon...

------------
**Threshold file**

You will need to pass in a YAML file containing pass/fail threshold tests for the metrics you are interested in. The file format consists of a list of objects each containing the following keys:

| Key | Value | Comments |
| --------------- | --------------- | --------------- |
| `metric_name`| Name of the metric to check| This can be any [supported metric](https://github.com/genome/qc-metric-aggregator/tree/master/process_metrics/metrics) and should be the value returned by `name`. |
| `operator` | Which operation to use to compare the metric value to the PASS/FAIL threshold| `<`,`<=`,`>`,`>=`, and `=` are all supported. If you instead specify `report` the metric will be reported in the final output, but not factored into the PASS/FAIL status. |
| `value` | The PASS/FAIL threshold to compare the metric value to | This field is optional if `report` is specified for the `operator`.|

An example can be [found here](https://github.com/genome/qc-metric-aggregator/blob/master/thresholds.yml.example)


------------
**Supported Metrics**

| Name  |  Description | Originating Tool  |
|---|---|---|
| FREEMIX | Freemix  |  VerifyBamId2 |
| Q20_BASES  |  Total bases with Q20 or higher | Picard CollectQualityYieldMetrics   |
| MEAN_COVERAGE  | Haploid Coverage  | Picard CollectWgsMetrics  |
| PCT_10X  | Percent coverage at 10x  | Picard CollectWgsMetrics  |
| PCT_20X  | Percent coverage at 20x  | Picard CollectWgsMetrics  |
| PCT_30X  | Percent coverage at 30x |  Picard CollectWgsMetrics |
| PCT_CHIMERAS   | Percent chimeras (PAIR)   | Picard CollectAlignmentSummaryMetrics  |
| READ1_PF_MISMATCH_RATE  |  Read 1 base mismatch rate | Picard CollectAlignmentSummaryMetrics  |
| READ2_PF_MISMATCH_RATE  |  Read 2 base mismatch rate |  Picard CollectAlignmentSummaryMetrics |
| MEDIAN_INSERT_SIZE  | Library insert size median  | Picard CollectInsertSizeMetrics  |
| MEDIAN_ABSOLUTE_DEVIATION  | Library insert size mad  | Picard CollectInsertSizeMetrics |
| PERCENT_DUPLICATION  | Percent duplicate marked reads  | Picard CollectDuplicateMetrics  |
| MEAN_TARGET_COVERAGE  | The mean coverage of a target region.  | Picard CollectHsMetrics  |
| PCT_TARGET_BASES_10X  | The fraction of all target bases achieving 10X or greater coverage | Picard CollectHsMetrics  |
| PCT_TARGET_BASES_20X  | The fraction of all target bases achieving 20X or greater coverage | Picard CollectHsMetrics  |
| PCT_TARGET_BASES_30X  | The fraction of all target bases achieving 30X or greater coverage |  Picard CollectHsMetrics |


------------
**Adding Additional Metrics**


To add support for additional metrics you simply need to subclass [Metric](https://github.com/genome/qc-metric-aggregator/blob/master/process_metrics/metrics/metric.py) and register it in [AvailableMetrics](https://github.com/genome/qc-metric-aggregator/blob/master/process_metrics/metrics/available_metrics.py)

Because many QC metrics are output in TSV format, there is a helper class [TSVMetric](https://github.com/genome/qc-metric-aggregator/blob/master/process_metrics/metrics/tsv_metric.py) that you can inherent from in addition to `Metric` that will make that easier. All of the currently supported metrics use this helper, so you should be able to look to them for examples.


