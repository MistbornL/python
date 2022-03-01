from services.functions import get_domain_ip


def test_get_domain_ip():
    hostnames = ["dns.google"]
    ip_adress = get_domain_ip(hostnames)
    assert ip_adress == ["8.8.4.4"]


