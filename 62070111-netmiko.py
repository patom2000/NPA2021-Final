from netmiko import *

device_ip = "10.0.15.105"
username = "admin"
password = "cisco"
device_param = {'device_type': "cisco_ios",
                'ip': device_ip, 
                'username': username,
                'password': password}

config_loopback_command = ["int loopback 62070111", "ip address 192.168.1.1 255.255.255.0"]
delete_loopback_command = ["no int loopback 62070111"]

def sendloopbackcommand(device, command):
    with ConnectHandler(**device) as ssh:
        result = ssh.send_config_set(command)
        result = ssh.send_command("sh ip int br")
        print(result)

def output_text_to_list(text):
    return text.strip().split("\n")

def check_loopback(device):
    with ConnectHandler(**device) as ssh:
        result = output_text_to_list(ssh.send_command("sh ip int br"))
        result.pop(0)
        interface = result[-1].split()
        if ("Loopback" in interface[0] and interface[1] == "unassigned") or "Loopback" not in interface[0]:
            return 0
        else:
            return 1

def delete_loopback(device):
    with ConnectHandler(**device) as ssh:
        exist = check_loopback(device)
        if exist == 1:
            sendloopbackcommand(device, delete_loopback_command)
        else:
            print("loopback is not exist")

def create_loopback(device):
    with ConnectHandler(**device) as ssh:
        exist = check_loopback(device)
        if exist == 0:
            sendloopbackcommand(device, config_loopback_command)
        else:
            print("loopback is already exist")

delete_loopback(device_param)
create_loopback(device_param)