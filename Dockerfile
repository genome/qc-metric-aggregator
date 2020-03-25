FROM python:alpine3.7

WORKDIR /qc

RUN pip install --upgrade pip
RUN pip install qc-metric-aggregator
