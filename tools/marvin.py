#!/opt/iot/python/bin/python3
# -*- coding: UTF-8 -*-

import datetime
from os import remove, path
from iotcore.home_presence import somebody_at_home
from devices.dreamebot import marvin
from time import sleep

SLEEP_INTERVAL = 60

CLEAN_HOURS = range(12, 20)
CLEAN_STATE_FILE = "/tmp/cleaned"


while True:
    if datetime.datetime.now().hour == 0 and datetime.datetime.now().minute == 0:
        remove(CLEAN_STATE_FILE)

    if datetime.datetime.now().hour in CLEAN_HOURS and path.isfile(CLEAN_STATE_FILE) is False and somebody_at_home() is False:
        open(CLEAN_STATE_FILE, 'a').close()
        print("Everybody left home! Start cleaning...")
        marvin.start()

    sleep(SLEEP_INTERVAL)
