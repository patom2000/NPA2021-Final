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

def add_message(message):
    url = 'https://webexapis.com/v1/messages'
    room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNTg4MjliOTAtOTE5Mi0xMWVjLWI3ZjMtODFlZDdmNGJiODhm"
    params = {'roomId': room_id, 'markdown': message}
    res = requests.post(url, headers=headers, json=params)
    print(res.json())

def list_room():
    url = "https://webexapis.com/v1/rooms/"
    headers = {
    "Authorization": f'Bearer {access_token}',
    "Content-Type": "application/json"
    }
    params = {
        "max":'100'
        }
    res = requests.get(url, headers=headers, params=params)
    print(json.dumps(res.json(), indent=4))

def get_message():
    amount = 1
    url = f"https://webexapis.com/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vNjUwODkzMjAtY2QxOS0xMWVjLWE1NGUtNGQ2MmNhMWM4YmVl&max={amount}"

    headers = {
        "Authorization": f'Bearer {access_token}',
        "Content-Type": "application/json"
    }
    res = requests.get(url, headers=headers)
    response_json = res.json()
    

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


"""add_message("6207011")
        time.sleep(1)
        Y2lzY29zcGFyazovL3VzL1JPT00vNjUwODkzMjAtY2QxOS0xMWVjLWE1NGUtNGQ2MmNhMWM4YmVl"""

get_message()