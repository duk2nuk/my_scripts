from netmiko import ConnectHandler
from pprint import pprint
import yaml

def connect_to_cisco_ios(device, command):
    with ConnectHandler(**device) as ssh:
        output = ssh.send_command(command, use_textfsm=True)
    return output

def open_file_device(filename):
    with open(filename) as file_settings:
        devices = yaml.safe_load(file_settings)
    return devices

command = "sh ip interface br"
if __name__ == "__main__":
    device = open_file_device("devices.yaml")
    result = []
    for one_device in device:
        result_ssh = connect_to_cisco_ios(one_device, command)
        result.append(result_ssh)
    pprint(result, width=120)
