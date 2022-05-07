from netmiko import *

device_ip = "10.0.15.105"
username = "admin"
password = "cisco"
device_param = {'device_type': "cisco_ios",
                'ip': device_ip, 
                'username': username,
                'password': password}

config_loopback = ["int loopback 62070111", "ip address 192.168.1.1 255.255.255.0"]

def set_loopback(device):
    with ConnectHandler(**device) as ssh:
        result = ssh.send_config_set(config_loopback)
        print(result)

        output = ssh.send_command("sh ip int br")
        print(output)


set_loopback(device_param)