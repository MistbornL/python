from services.functions import get_domain_ip, get_domain_name, writer

if __name__ == "__main__":
    hostnames, ip_adresses = [], []
    get_domain_name(["8.8.8.8", "13.251.106.90"], hostnames)
    writer("names.txt", "w", hostnames)
    get_domain_ip(["dns.google", "ec2-13-251-106-90.ap-southeast-1.compute.amazonaws.com"], ip_adresses)
    writer("ips.txt", "w", ip_adresses)
