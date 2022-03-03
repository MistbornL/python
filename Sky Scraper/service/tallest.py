"""[
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]"""


def tallest_skyscraper(buildings):
    info = {}
    for row in buildings:
        for building in range(len(row)):
            if row(building) == 1:
                info.update({row(building): 1})
    return info
