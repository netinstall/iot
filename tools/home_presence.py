#!/opt/iot/python/bin/python3
# -*- coding: UTF-8 -*-

from iotcore.home_presence import save_home_presence
from time import sleep


SLEEP_INTERVAL = 30

while True:
    save_home_presence()
    sleep(SLEEP_INTERVAL)
