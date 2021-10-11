from random import choice


players = [
    {"name": "nika", "mail": "nika@gmail.com", "sex": "M"},
    {"name": "lasha", "mail": "lasha@gmail.com", "sex": "M"},
    {"name": "saba", "mail": "saba@gmail.com", "sex": "M"},
    {"name": "beka", "mail": "beka@gmail.com", "sex": "M"},
    {"name": "ekaterine", "mail": "ekaterine@gmail.com", "sex": "F"},
    {"name": "lile", "mail": "lile@gmail.com", "sex": "F"}
]


def get_players_by_sex(sex):
    p = []
    for player in players:
        if player["sex"] == sex:
            p.append(player)
    return p


males, females = get_players_by_sex("M"), get_players_by_sex("F")
pairs = []


while males:
    male = choice(males)
    males.remove(male)
    if females:
        female = choice(females)
        females.remove(female)
        pairs.append([male, female])
    else:
        second_male = choice(males)
        males.remove(second_male)
        pairs.append([male, second_male])


for pair in pairs:
    print(pair[0]["name"], "&", pair[1]["name"])
