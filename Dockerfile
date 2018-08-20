FROM continuumio/miniconda3

WORKDIR /workspace
RUN mkdir assets

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /workspace
