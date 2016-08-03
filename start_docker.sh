#!/usr/bin/env bash

#docker pull ermaker/keras-jupyter

docker run -d -p 8888:8888 -e KERAS_BACKEND=tensorflow -v $(pwd)/notebook:/notebooks tensorflow/tensorflow
