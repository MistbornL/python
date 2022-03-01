from services.functions import writer


def test_check_writer():
    ip_adresses = ["8.8.8.8"]
    writer("test.txt", 'w', ip_adresses)

    with open("test.txt") as file:
        assert file.readline().strip() == ip_adresses[0]
