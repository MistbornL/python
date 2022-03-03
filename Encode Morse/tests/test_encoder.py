from service.encode_morse import encode_morse
from materials.example import char_to_dots


def test_encode_morse():
    example = ".... . .-.. .--.  -- .  -.-.--"
    assert example == encode_morse("HELP ME !", char_to_dots)
