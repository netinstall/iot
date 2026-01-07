from yandex import iot


class socket():

    def __init__(self, device_id=None):
        self.id = device_id
        self.name = iot.get_device(self.id)["name"]

    def state(self):
        return iot.get_device(self.id)["capabilities"][0]["state"]["value"]

    def state_html(self):
        state = ""
        if self.state():
            state = "checked"
        return state

    def power_control(self, state):
        if type(state) == str:
            state = True if state == "true" else False
        return iot.set_device_state(self.id, state)


class thermostat(socket):

    def get_temperature(self):
        return iot.get_device(self.id)["capabilities"][1]["state"]["value"]

    def set_temperature(self, temperature):
        return iot.set_device_state(self.id, temperature, action_type="devices.capabilities.range", instance="temperature")



class controller():

    def __init__(self, device_id, action_map):
        self.id = device_id
        self.action_map = action_map

    def get_state(self):
        return iot.get_device(self.id)["capabilities"][1]["state"]["value"]

    def reset_state(self):
        return iot.set_device_state(self.id, 16, action_type="devices.capabilities.range", instance="temperature")

    def get_action(self):
        action = self.action_map.get(self.get_state())
        self.reset_state()
        return action

    def get_action_map(self):
        return self.action_map

