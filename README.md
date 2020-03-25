    usage: aggregate-qc-metrics [-h] -o OUTPUT_PATH -t THRESHOLD_FILE
                                sample_name metrics_dir

    positional arguments:
      sample_name           The sample name or id for which the QC metrics apply
      metrics_dir           The directory to search for metric files, often a
                            cromwell run directory

    optional arguments:
      -h, --help            show this help message and exit

    named arguments:
      -o OUTPUT_PATH, --output-path OUTPUT_PATH
                            File path to store the finalized mertrics TSV
      -t THRESHOLD_FILE, --threshold-file THRESHOLD_FILE
                            Path to the yml thresholds file to validate against

