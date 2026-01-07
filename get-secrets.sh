#!/bin/bash

APP="iot"

source /opt/vault/bw-wrapper.sh

mkdir -p secrets; cd secrets
get_secret marvin.py
get_secret mikrotik.py
get_secret tion.py
get_secret yandex.py
