from typing import List


def game_over(player: List, computer: List, deck: List):
    if len(deck) == 0:
        if len(player) > len(computer):
            print("you Loose!")
        elif len(player) < len(computer):
            print("You Win!")
        else:
            print("Draw!")
