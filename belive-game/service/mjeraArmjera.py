from typing import List


def mjera_armjera(p1: List, p2: List, table: List, guess: List):
    print(f"Player shows cards {table}")
    if sorted(table) == sorted(guess):
        p1.extend(table)
        table.clear()
        guess.clear()
    else:
        p2.extend(table)
        table.clear()
        guess.clear()
