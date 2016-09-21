FROM tensorflow/tensorflow

MAINTAINER Mihail Chirita <mihailrc@gmail.com>

RUN pip install --upgrade pip

RUN pip --no-cache-dir install \
        keras \
        scikit-learn \
