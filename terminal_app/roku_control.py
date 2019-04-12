"""Roku controller functions that wrap http requests, returning status codes"""
import requests
import xmltodict
import json
ROKU_URL = "http://192.168.1.10:8060/"
KEYS = [
    "up",
    "down",
    "left",
    "right",
    "select",
    "fwd",
    "rev",
    "backspace",
    "enter",
    "back",
    "play",
    "home"
]
def send_keypress(key_string):
    """Send a key/button press via HTTP"""
    response = requests.post((ROKU_URL+"keypress/"+key_string))
    return response.status_code

def get_channels():
    response = requests.get((ROKU_URL+"query/apps"))
    apps = json.loads(json.dumps(xmltodict.parse(response.content)))
    apps = apps["apps"]["app"]
    new_apps = []
    for app in apps:
        new_apps.append({"name":app["#text"],"id":app["@id"]})
    return new_apps

def launch_app(app_id):
    """Launch an application via HTTP"""
    response = requests.post((ROKU_URL+"launch/"+app_id))
    return response.status_code
