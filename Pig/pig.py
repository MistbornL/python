from service.generate import generate_deck
from service.playerDraw import player_draw_card
from service.computerDraw import computer_draw_card
from service.gameOver import game_over
from service.nextmove import next_move

forms = ['diamonds', 'spades', 'clubs', 'hearts']
numbers = ['friends', '2', '3', '4', '5', '6', '7', '8', '9', 'jack', 'queen', 'king', 'ace']
deck, player, computer, obshiak = [], [], [], []


def main():
    generate_deck(deck, forms, numbers)
    while len(deck) > 0:
        player_draw_card(deck, player, obshiak)
        computer_draw_card(deck, computer, obshiak)
        next_move()

        if game_over(player, computer, deck):
            break


if __name__ == "__main__":
    main()
