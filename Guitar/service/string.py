def string_fret(st, fr, notes, strings):
    if st not in range(1, 7) or fr > 24:
        return 'Invalid input'
    return notes[(notes.index(strings[st]) + fr) % 12]