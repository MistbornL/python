from service.playerChoiceCards import player_choice_cards
from service.shuffle import shuffle_cards
from service.playerNumber import player_number
from service.mjeraArmjeraDamateba import mjera_armjera_damateba1, mjera_armjera_damateba2

deck = [
    '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'js', 'qs', 'ks', 'as',
    '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'jh', 'qh', 'kh', 'ah',
    '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'jd', 'qd', 'kd', 'ad',
    '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'jc', 'qc', 'kc', 'ac'
]

table = []
p1, p2, p3, p4 = [], [], [], []


turn = 1


def main():
    shuffle_cards(deck)
    player_number(deck, p1, p2, p3, p4)
    while True:
        global turn
        if turn == 1:
            print("Player 1")
            player_choice_cards(p1, table)
            mjera_armjera_damateba1(p1, p2, table)
            turn += 1
        elif turn == 2:
            print("Player 2")
            player_choice_cards(p2, table)
            mjera_armjera_damateba2(p2, p1, table)
            turn -= 1


if __name__ == "__main__":
    main()
