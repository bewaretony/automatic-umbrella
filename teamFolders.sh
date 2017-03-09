#!/bin/sh

python $(dirname $0)/teamList.py 2017utwv | xargs -d '\n' mkdir
