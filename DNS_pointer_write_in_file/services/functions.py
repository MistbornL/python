from typing import List
import socket


def get_domain_name(ip_address: List, hostnames: List):
    for ip in ip_address:
        result = socket.gethostbyaddr(ip)
        hostnames.append(result[0])
    return hostnames


def get_domain_ip(hostnames: List, ip_adresses):
    for name in hostnames:
        result = socket.gethostbyname(name)
        ip_adresses.append(result)
    return ip_adresses


def writer(file_name, option, target_list):
    with open(file_name, option) as file:
        for item in target_list:
            file.writelines(item)
            file.writelines("\n")
