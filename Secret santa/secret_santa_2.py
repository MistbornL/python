from random import choice
import csv

p, players = [], []
with open("myFile0.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        players.append((row[1], row[2]))
    players.pop(0)
    print(players)
    try:
        for i in range(len(players)):
            choice1 = choice(players)
            players.remove(choice1)
            choice2 = choice(players)
            players.remove(choice2)
            p.append((choice1, choice2))
    except IndexError:
        pass

    with open('data.csv', 'w', newline='') as csv_write:
        writer = csv.writer(csv_write)
        for pair in p:
            data = pair[0][0], pair[1][0]
            writer.writerow(data)
