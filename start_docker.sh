#!/usr/bin/env bash

docker run --rm -it -p 8888:8888 \
  -v $(pwd)/notebooks:/tf/notebooks -v $(pwd)/data:/data \
  -v $(pwd)/models:/models mihailrc/deep-learning
