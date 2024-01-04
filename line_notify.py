import requests
from main import *

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return r.status_code


# 傳送的訊息內容
message = message()
token = 'QIJRF8uA1ya7zvXxTDGNQxWyUJtaE9Sl4FuEb3X6QDI'

lineNotifyMessage(token, message)




# QIJRF8uA1ya7zvXxTDGNQxWyUJtaE9Sl4FuEb3X6QDI