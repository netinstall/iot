import os

IOT_PATH = "/opt/iot/"
IOT_TMP_PATH = IOT_PATH + ".tmp/"

if not os.path.exists(IOT_TMP_PATH):
    os.mkdir(IOT_TMP_PATH)
