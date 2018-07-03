FROM continuumio/miniconda3

WORKDIR /workspace
RUN mkdir assets

RUN pip install --upgrade pip && \
    pip install flask-restplus

COPY . /workspace
