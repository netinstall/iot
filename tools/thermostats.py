#!/opt/iot/python/bin/python3
# -*- coding: UTF-8 -*-

import datetime
from iotcore.home_presence import somebody_at_home
from devices import thermostats
from time import sleep

SLEEP_INTERVAL = 600

def thermostat_turn_off(ts):
    if ts.state() is True:
        ts.power_control(False)
        print("Turning off thermostat: {}".format(ts.id))

while True:
    if somebody_at_home() is False:
        thermostat_turn_off(thermostats.ts_bedroom)
        thermostat_turn_off(thermostats.ts_living_room)

    sleep(SLEEP_INTERVAL)
