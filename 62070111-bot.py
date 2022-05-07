from cgitb import enable
from email import message
import requests
import json
import time
access_token = "NDRhM2RlNjAtOWM1Mi00MTIwLWFjZTUtZTI3MmU4OTk5ZjE5M2Y3NWQwNDktNTdh_P0A1_4a252141-f787-4173-a4c9-bde69c553a24"

headers = {
 'Authorization': f'Bearer {access_token}',
 'Content-Type': 'application/json'
}
main_room = "Y2lzY29zcGFyazovL3VzL1JPT00vNjUwODkzMjAtY2QxOS0xMWVjLWE1NGUtNGQ2MmNhMWM4YmVl"
test_room = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNTg4MjliOTAtOTE5Mi0xMWVjLWI3ZjMtODFlZDdmNGJiODhm"

def add_message(message, room_id):
    url = 'https://webexapis.com/v1/messages'
    params = {'roomId': room_id, 'markdown': message}
    requests.post(url, headers=headers, json=params)

def list_room():
    url = "https://webexapis.com/v1/rooms/"
    params = {
        "max":'100'
        }
    res = requests.get(url, headers=headers, params=params)
    print(json.dumps(res.json(), indent=4))

def get_message(room_id):
    amount = 1
    url = f"https://webexapis.com/v1/messages?roomId={room_id}&max={amount}"
    res = requests.get(url, headers=headers)
    response_json = res.json()
    return response_json['items'][0]['text']

def check_loopback_status():
    device_ip = "10.0.15.105"
    api_url = f"https://{device_ip}/restconf/data/ietf-interfaces:interfaces"
    headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
    }
    basicauth = ("admin", "cisco")
    resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
    response_json = resp.json()
    status = response_json['ietf-interfaces:interfaces']['interface'][-1]['enabled']
    name = response_json['ietf-interfaces:interfaces']['interface'][-1]['name']
    return status, name

def core_bot(room_id):
    add_message("start", room_id)
    while 1:
        time.sleep(1)
        text = get_message(room_id)
        if text == "62070111":
            status, name = check_loopback_status()
            if status == 1:
                add_message(f"{name} - Operational status is up", room_id)
            if status == 0:
                add_message(f"{name} - Operational status is down", room_id)


core_bot(main_room)