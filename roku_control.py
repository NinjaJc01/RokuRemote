import requests
ROKU_URL = "http://192.168.1.10:8060/"

def sendKeypress(key_string):
    a = requests.post((ROKU_URL+"keypress/"+key_string))
    print(a.status_code)
sendKeypress("play")