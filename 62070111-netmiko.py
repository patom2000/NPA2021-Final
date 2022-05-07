from netmiko import *

device_ip = "10.0.15.105"
username = "admin"
password = "cisco"
device_param = {'device_type': "cisco_ios",
                'ip': device_ip, 
                'username': username,
                'password': password}

config_loopback = ["int loopback 62070111", "ip address 192.168.1.1 255.255.255.0"]
delete_loopback = ["no int loopback 62070111"]

def sendloopbackcommand(device, command):
    with ConnectHandler(**device) as ssh:
        result = ssh.send_config_set(command)
        result = output_text_to_list(ssh.send_command("sh ip int br"))
        print(result)

def output_text_to_list(text):
    return text.strip().split("\n")

def check_loopback(device, readytodel = 0, readytoconfig = 0):
    with ConnectHandler(**device) as ssh:
        result = output_text_to_list(ssh.send_command("sh ip int br"))
        result.pop(0)
        interface = result[-1].split()
        if "Loopback" in interface[0]:
            readytodel = 1
        if ("Loopback" in interface[0] and interface[1] == "unassigned") or "Loopback" not in interface[0]:
            readytoconfig = 1
        if readytoconfig:
            ans = input("Do you want to create loopback?(Y or N): ")
            if ans == "y" or ans == "Y":
                sendloopbackcommand(device, config_loopback)
            readytodel = 1
            readytoconfig = 0
        if readytodel:
            ans = input("Do you want to delete loopback?(Y or N): ")
            if ans == "y" or ans == "Y":
                sendloopbackcommand(device, delete_loopback)

check_loopback(device_param)
