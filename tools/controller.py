#!/opt/iot/python/bin/python3
# -*- coding: UTF-8 -*-

from time import sleep
from devices.controller import controller
from devices.dreamebot import marvin
from settings.marvin import CORRIDOR_CARPET, BEDROOM

from iotcore.brightness import is_dark
from devices.lamps import floor_lamp, kitchen_lamp

SLEEP_INTERVAL = 10


while True:
    action = controller.get_action()
    if action == "clean_bedroom":
        print("Clean bedroom")
        marvin.start_clean_rooms(BEDROOM)
    if action == "clean_carpet":
        print("Clean carpet")
        marvin.start_clean_rooms(CORRIDOR_CARPET)
    if action == "turn_on_floor_lamp":
        print("turn_on_floor_lamp")
        if is_dark():
            floor_lamp.power_control(True)
            kitchen_lamp.power_control(True)
            print("Turning on lamps")


    sleep(SLEEP_INTERVAL)
