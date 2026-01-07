#!/bin/bash

APP="iot"

source /opt/vault/bw-wrapper.sh

cd settings
get_secret marvin.py
get_secret mikrotik.py
get_secret tion.py
get_secret yandex.py
