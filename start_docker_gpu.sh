#!/usr/bin/env sh

docker run --rm -it --gpus all -p 8888:8888 \
  -v $(pwd)/notebooks:/tf/notebooks -v $(pwd)/data:/data \
  -v $(pwd)/models:/models mihailrc/deep-learning-gpu
