def encode_morse(code: str, sequence: dict):
    to_morse = ""
    for letter in code:
        letter = letter.upper()
        if letter in sequence:
            if letter == " ":
                to_morse += " "
            else:
                to_morse += " " + sequence[letter]
    return to_morse.strip()
