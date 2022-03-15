from service.string import string_fret
notes = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', "A", "A#/Bb", "B"]
strings = {6:'E', 5:'A', 4:'D', 3:'G', 2:'B', 1:'E'}


def main():
    print(string_fret(1, 7, notes, strings))


if __name__ == "__main__":
    main()
