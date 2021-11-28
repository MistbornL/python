import random

from typing import List


def computer_draw_card(deck: List, computer: List, obshiak: List):
    if len(computer) == 0:
        card = random.choice(deck)
        deck.remove(card)
        obshiak.append(card)

        kind, number = card
        print(f"computer: {number} of {kind}")

        if len(obshiak) > 1 and obshiak[len(obshiak) - 2][0] == obshiak[len(obshiak) - 1][0]:
            print("Computer Picks Cards!!")
            computer.extend(obshiak[:])
            obshiak.clear()
            return obshiak
    elif len(computer) == 1:
        card = computer[0]
        kind, number = card
        obshiak.append(card)
        print(f"Computer: {number} of {kind}")
        computer.remove(card)

        if len(obshiak) > 1 and obshiak[len(obshiak) - 2][0] == obshiak[len(obshiak) - 1][0]:
            print("Computer Picks Cards!!")
            computer.extend(obshiak[:])
            obshiak.clear()
            return obshiak
    elif len(computer) > 1:
        computer_choice = random.randrange(1, len(computer))
        card = computer[computer_choice]

        kind, number = card
        obshiak.append(card)
        print(f"Computer: {number} of {kind}")
        computer.remove(card)

        if len(obshiak) > 1 and obshiak[len(obshiak) - 2][0] == obshiak[len(obshiak) - 1][0]:
            print("Computer Picks Cards!!")
            computer.extend(obshiak[:])
            obshiak.clear()
            return obshiak