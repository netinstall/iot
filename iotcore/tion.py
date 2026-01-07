import datetime
import json
import requests
import settings
from iotcore import api
from settings.tion import EMAIL, PASSWORD


TION_API_URL = "https://api2.magicair.tion.ru"
TION_OAUTH_FILE = settings.IOT_TMP_PATH + "tion.json"

class magic_air():


    def __init__(self, mac=None):
        self.update_before_expire_days = 10
        self.mac = mac


    def get_oauth_data(self):
        with open(TION_OAUTH_FILE) as f:
            return json.loads(f.read())


    def get_oauth_token(self):
        return  self.get_oauth_data()["access_token"]


    def tion_request(self, path, method="get", data=None, auth_headers=True):
        headers = None
        if auth_headers:
            headers = {"Authorization": "Bearer " + self.get_oauth_token()}
        return api.request(TION_API_URL + path, headers=headers, method=method, data=data)


    def get_token(self, update=False):
        data = {
            "client_id": "cd594955-f5ba-4c20-9583-5990bb29f4ef",
            "client_secret": "syRxSrT77P",
        }

        if update:
            expires_datetime_raw = (self.get_oauth_data()[".expires"])
            expires_date = expires_datetime_raw.split("T")[0]
            expires_datetime = datetime.datetime.strptime(
                expires_date, '%Y-%m-%d').date()
            # Проверяем, скоро ли протухнет токен:
            days_to_expire = expires_datetime - datetime.date.today()
            print("Days to expire: %s" % days_to_expire)
            if((days_to_expire > datetime.timedelta(days=self.update_before_expire_days))):
                exit()
            refresh_token = self.get_oauth_data()["refresh_token"]
            data["grant_type"] = "refresh_token"
            data["refresh_token"] = refresh_token
        else:
            data["username"] = EMAIL
            data["password"] = PASSWORD
            data["grant_type"] = "password"
        oauth_data = self.tion_request("/idsrv/oauth2/token", method="post", data=data, auth_headers=False)
        print(oauth_data)
        with open(TION_OAUTH_FILE, "w") as f:
            json.dump(oauth_data, f)
        print("Updated: %s" % TION_OAUTH_FILE)


    def set_zone_mode(self, zone_id, mode):
        return self.tion_request("/zone/" + zone_id + "/mode", {"mode": mode,"co2":700}, method="post")


    def set_device_mode(self, device_id, mode):
        return self.tion_request("/device/" + device_id + "/mode", data=mode, method="post")


    def get_device_data(self):
        tion_data = self.tion_request("/location")
        for house in tion_data:
            for zone in house["zones"]:
                for device in zone["devices"]:
                    if device["mac"] == self.mac:
                        return device["data"]


    def humidity(self):
        return float(self.get_device_data()["humidity"])


    def temperature(self):
        return float(self.get_device_data()["temperature"])


    def co2(self):
        return float(self.get_device_data()["co2"])
