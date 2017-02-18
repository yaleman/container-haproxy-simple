#!/bin/bash

# sets up the virtual environment
virtualenv -p python3 venv
# loads it
source venv/bin/activate
# installs the required packages
pip install -r requirements.txt
