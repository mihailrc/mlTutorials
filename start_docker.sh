#!/usr/bin/env bash

docker run --rm -it -p 8888:8888 -e KERAS_BACKEND=tensorflow \
  -v $(pwd)/notebooks:/notebooks -v $(pwd)/data:/data \
  -v $(pwd)/models:/models mihailrc/deep-learning
