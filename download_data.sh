#!/usr/bin/env sh

curl -L https://s3-us-west-1.amazonaws.com/udacity-selfdrivingcar/traffic-signs-data.zip -o traffic-signs-data.zip
unzip traffic-signs-data.zip -d data/traffic-signs-data
rm traffic-signs-data.zip
