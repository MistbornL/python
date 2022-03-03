from service.encode_morse import encode_morse
from materials.example import char_to_dots


def main():
    print(encode_morse("HELP ME !", char_to_dots))


if __name__ == "__main__":
    main()

