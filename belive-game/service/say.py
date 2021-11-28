from typing import List


def player1_say(guess: List):
    decision = input("P1 // I have: ")
    guess.extend(decision.split(" "))


def player2_say(guess: List):
    decision = input("P2 // I have: ")
    guess.extend(decision.split(" "))