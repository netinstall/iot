import json
from iotcore import api
from secrets import YANDEX_IOT_OAUTH_TOKEN

YANDEX_IOT_API = "https://api.iot.yandex.net/v1.0"


def iot_request(path, method="get", data=None):
    iot_headers = {"Authorization": "Bearer " + YANDEX_IOT_OAUTH_TOKEN}
    return api.request(YANDEX_IOT_API + path, headers=iot_headers, method=method, data=data)


def get_rooms_list():
    return iot_request("/user/info")["rooms"]


def get_devices_id_list():
    device_list = []
    for room in get_rooms_list():
        for device in room["devices"]:
            device_list.append(device)
    return device_list


def get_device(device_id):
    return iot_request("/devices/" + device_id)


def set_device_state(device_id, state, action_type="devices.capabilities.on_off", instance="on"):
    data = {"actions": [{"type": action_type,
                         "state": {"instance": instance, "value": state}}]}
    data = json.dumps(data)
    result = iot_request("/devices/" + device_id + "/actions", method="post", data=data)
    return result


# Deprecated:
def run_scenario(scenario_id):
    csrf_token_header = {
        "x-csrf-token": get_yandex_iot_csrf_token()}
    result = yandex.request(YANDEX_IOT_API + "/scenarios/" + scenario_id +
                            "/actions", method="post", headers=csrf_token_header)
    return result

