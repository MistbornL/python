from typing import List

from mjeraarmjera.service.say import player1_say, player2_say
from mjeraarmjera.service.mjeraArmjera import mjera_armjera
from mjeraarmjera.service.playerChoiceCards import player_choice_cards
guess = []
loop = True


def mjera_armjera_damateba1(p1: List, p2: List, table: List):
    global loop
    while loop:
        player1_say(guess)
        choice = input("Choose From This Options Mjera/Ar Mjera/Damateba: ")

        if choice == "mjera":
            mjera_armjera(p1, p2, table, guess)
            break
        elif choice == "ar mjera":
            print(p2)
            mjera_armjera(p2, p1, table, guess)
            print(p2)
            break
        elif choice == "damateba":
            player_choice_cards(p2, table)
            mjera_armjera_damateba2(p1, p2, table)
            break


def mjera_armjera_damateba2(p1: List, p2: List, table: List):
    global loop
    while loop:
        player2_say(guess)
        choice = input("Choose From This Options Mjera/Ar Mjera/Damateba: ")

        if choice == "mjera":
            mjera_armjera(p2, p1, table, guess)
            break
        elif choice == "ar mjera":
            mjera_armjera(p1, p2, table, guess)
            break
        elif choice == "damateba":
            player_choice_cards(p2, table)
            mjera_armjera_damateba2(p1, p2, table)
            break
