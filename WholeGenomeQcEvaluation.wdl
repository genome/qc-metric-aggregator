version 1.0

task AggregateQcMetrics {
  input {
    File metrics_directory
    File thresholds_file
    String sample_id
    String output_file_name
    Int preemptible_tries
  }

  command {
    aggregate-qc-metrics ~{sample_id} \
    ~{metrics_directory} \
    ~{output_file_name} \
    ~{thresholds_file}
  }

  runtime {
    docker: "mgibio/qc-metric-aggregator:0.1.2"
    disks: "local-disk 2 HDD"
    memory: "2 GiB"
    preemptible: preemptible_tries
  }

  output {
    File qc_values = "~{output_file_name}"
  }
}

workflow EvaluateWholeGenomeQcMetrics {
  input {
    File metrics_directory
    File thresholds_file
    String sample_id
    String output_file_name
    Int preemptible_tries
  }


  call AggregateQcMetrics {
    input:
      metrics_directory = metrics_directory,
      thresholds_file = thresholds_file,
      sample_id = sample_id,
      output_file_name = output_file_name,
      preemptible_tries = preemptible_tries
  }

  output {
    File qc_values = AggregateQcMetrics.qc_values
  }
}
