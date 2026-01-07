import json
import os
from devices import mikrotik
from settings import IOT_TMP_PATH, PERSONAL_DEVICES_MACS


HOME_PRESENCE_FILE = IOT_TMP_PATH + "home_presence.json"

def get_users_presence():
    users_presence = {}
    mikrotik_lease_macs = mikrotik.get_lease_macs()
    print(mikrotik_lease_macs)
    for user, mac in PERSONAL_DEVICES_MACS.items():
        at_home = True if mac in mikrotik_lease_macs else False
        users_presence[user] = at_home
    return users_presence


def get_home_presence():
    if not os.path.isfile(HOME_PRESENCE_FILE):
        save_home_presence(init=True)
    with open(HOME_PRESENCE_FILE) as f:
        return json.loads(f.read())


def somebody_at_home():
    if True in get_home_presence().values():
        return True
    return False

def save_home_presence(init=False):
    just_came = False
    prev_home_presence = None if init else get_home_presence()
    home_presence = get_users_presence()
    if prev_home_presence is not None:
        if True not in prev_home_presence.values():
            if True in home_presence.values():
                just_came = True
    home_presence["just_came"] = just_came
    print(home_presence)
    with open(HOME_PRESENCE_FILE, "w") as f:
        json.dump(home_presence, f)

