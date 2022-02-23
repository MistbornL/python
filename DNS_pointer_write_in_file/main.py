from services.functions import get_domain_ip, get_domain_name, writer

if __name__ == "__main__":
    ip_adresses = ["8.8.8.8", "13.251.106.90"]
    names = ["dns.google", "ec2-13-251-106-90.ap-southeast-1.compute.amazonaws.com"]
    hostnames = get_domain_name(ip_adresses)
    writer("names.txt", "w", hostnames)
    ip_adress = get_domain_ip(names)
    writer("ips.txt", "w", ip_adress)
