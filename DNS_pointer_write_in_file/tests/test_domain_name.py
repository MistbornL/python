from services.functions import get_domain_name


def test_get_domain_name():
    ip_adresses = ["8.8.8.8"]
    hostnames = get_domain_name(ip_adresses)
    assert hostnames == ["dns.google"]


