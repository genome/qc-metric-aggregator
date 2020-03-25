from setuptools import setup

setup(
    name = 'qc-metric-aggregator',
    description = 'Given the output directory of a QC pipeline and a threshold config file, parse out the desired metrics and evalute them against the thresholds.',
    author = 'Adam Coffman',
    author_email = 'acoffman@wustl.edu',
    version = '0.1.0',
    packages = ['process_metrics'],
    install_requires = [
        'pyyaml'
    ],
    entry_points = {
        'console_scripts': [
            'aggregate-qc-metrics = process_metrics.__main__:generate_report'
        ]
    })
