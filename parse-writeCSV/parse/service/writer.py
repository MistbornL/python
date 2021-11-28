import csv
from typing import List


def writer(filename: str, header: List, data: List):
    with open(filename, 'w', newline='', encoding="utf-8") as f:
        wr = csv.writer(f, delimiter=",")

        wr.writerow(header)
        wr.writerow(data)
