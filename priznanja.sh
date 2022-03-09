#!/bin/sh
source ./venv/Scripts/activate
#  Pokličemo priznanja.py in dodamo argument 'dist',
#  ki pove, v kateri podmapi so zunanje datoteke ...
python ./priznanja.py dist
source ./venv/Scripts/deactivate
