FROM continuumio/miniconda3

WORKDIR /workspace
RUN mkdir assets

ARG flask_restplus_version=0.11.0

RUN pip install --upgrade pip && \
    pip install flask-restplus==${flask_restplus_version}

COPY . /workspace
