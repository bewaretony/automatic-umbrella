#!/bin/sh

TEAM_DIR=$(python $(dirname $0)/VARS.py teamDir)
mkdir -p $TEAM_DIR
mkdir -p $(python $(dirname $0)/VARS.py videoDir)
python $(dirname $0)/teamDirNames.py $1 | xargs -d '\n' mkdir -p
