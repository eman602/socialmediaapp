#!/bin/bash

sudo apt install python3-pip

python3 -m pip install --user virtualenv

python3 -m venv env

. env/bin/activate

pip install -r requirements.txt