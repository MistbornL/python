import random

from typing import List


def player_draw_card(deck: List, player: List, obshiak: List):
    if len(player) == 0:
        card = random.choice(deck)
        deck.remove(card)
        obshiak.append(card)

        kind, number = card
        print(f"Player: {number} of {kind}")

        if len(obshiak) > 1 and obshiak[len(obshiak) - 2][0] == obshiak[len(obshiak) - 1][0]:
            print("Player Picks Cards!!")
            player.extend(obshiak[:])
            obshiak.clear()
    elif len(player) > 0:
        while True:
            try:
                print(f"Your options {player}")
                quest = int(input("Enter index: "))
                card = player[quest]

                kind, number = card
                print(f"Player: {number} of {kind}")
                obshiak.append(card)
                player.remove(card)
                if len(obshiak) > 1 and obshiak[len(obshiak) - 2][0] == obshiak[len(obshiak) - 1][0]:
                    print("Player Picks Cards!!")
                    player.extend(obshiak[:])
                    obshiak.clear()
                break
            except IndexError:
                print("Enter valid Index!!")
                continue
            except ValueError:
                print("Enter valid Index!!")
                continue
