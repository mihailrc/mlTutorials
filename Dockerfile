FROM tensorflow/tensorflow:latest-py3-jupyter

MAINTAINER Mihail Chirita <mihailrc@gmail.com>

RUN pip install --upgrade pip

RUN pip --no-cache-dir install \
        scikit-learn \
