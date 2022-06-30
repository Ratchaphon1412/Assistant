#!/bin/bash

brew install portaudio
python3 -m venv AssistantEnv
source AssistantEnv/bin/activate
pip3 install -r requirements.txt
pip3 install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' PyAudio
