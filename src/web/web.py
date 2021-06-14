#!/opt/iot/python/bin/python3
# -*- coding: UTF-8 -*-

import requests
import time
from bottle import route, run, request, response, redirect, template, TEMPLATE_PATH, HTTPResponse
from iot import devices
from iot import yandex_iot
from iot import settings


YANDEX_AUTH_PAGE = "https://oauth.yandex.ru/authorize?response_type=token&client_id=" + \
    settings.YANDEX_OAUTH_CLIENT_ID
YANDEX_OAUTH_API = "https://login.yandex.ru/info?oauth_token="

TEMPLATE_PATH.append("./html")


def get_yandex_oauth_info(token):
    return requests.get(YANDEX_OAUTH_API + token).json()


def check_auth():
    yandex_oauth_token = request.get_cookie("ytkn")
    if not yandex_oauth_token:
        redirect(YANDEX_AUTH_PAGE)
    yandex_oauth_info = get_yandex_oauth_info(yandex_oauth_token)
    if yandex_oauth_info.get("login") not in settings.YANDEX_ALLOW_USERS:
        return False
    return True


@route("/oauth_token/", method="GET")
def oauth_token():
    return template("oauth_token.html")

@route("/ping", method="GET")
def ping():
    return "pong"


@route("/", method="GET")
def root():
    if not check_auth():
        return HTTPResponse(status=403)
    return template("devices.tpl", devices=devices.home_devices)


@route("/action/tv/source", method="POST")
def tv_action():
    if not check_auth():
        return HTTPResponse(status=403)
    devices.tv.select_source(request.POST.get("source"))
    return HTTPResponse(status=200)


@route("/action/power_control", method="POST")
def pc_action():
    if not check_auth():
        return HTTPResponse(status=403)
    device_name = request.POST.get("device")
    action = request.POST.get("action")
    device = devices.home_devices[device_name]
    device.power_control(action)
    if device_name == "london" and action == "true":
        devices.tv.power_control("wakeup")
        time.sleep(3)
        devices.tv.select_source("pc")
    return HTTPResponse(status=200)


@route("/action/temperature_control", method="POST")
def temperature_control():
    temperature = int(request.POST.get("temperature"))
    print(temperature)
    devices.thermostat.set_temperature(temperature)
    return HTTPResponse(status=200)

if __name__ == "__main__":
    run(host='::', port=8080, debug=True)
