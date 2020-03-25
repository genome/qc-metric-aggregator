import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name = 'qc-metric-aggregator',
    description = 'Given the output directory of a QC pipeline and a threshold config file, parse out the desired metrics and evalute them against the thresholds.',
    long_description=README,
    long_description_content_type="text/markdown",
    author = 'Adam Coffman',
    author_email = 'acoffman@wustl.edu',
    version = '0.1.2',
    license = 'MIT',
    url = 'https://github.com/genome/qc-metric-aggregator',
    packages = [
        'process_metrics',
        'process_metrics.metrics'
        ],
    install_requires = [
        'pyyaml'
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points = {
        'console_scripts': [
            'aggregate-qc-metrics = process_metrics.__main__:generate_report'
        ]
    })
