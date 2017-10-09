#!/bin/bash

# make virtual env to hold python packages for project
mkdir -p venv/py3
cd venv
python3 -m venv py3
cd ../
source venv/py3/bin/activate

# install necessary python libs
cd scripts
pip install -e .

# activate venv
cd ../
source venv/py3/bin/activate