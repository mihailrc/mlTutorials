FROM tensorflow/tensorflow:latest-py3-jupyter

MAINTAINER Mihail Chirita <mihailrc@gmail.com>

COPY jupyter_notebook_config.json /root/.jupyter/

RUN pip install --upgrade pip

RUN pip --no-cache-dir install \
        scikit-learn \
