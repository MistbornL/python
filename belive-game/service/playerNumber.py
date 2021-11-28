from typing import List
import numpy as np


def player_number(deck: List, p1: List, p2: List, p3: List, p4: List):
    while True:
        try:
            parts = []
            question = int(input("Choose Number Of Players: "))
            splited = np.array_split(deck, question)

            if len(splited) % 2 == 0:
                for array in splited:
                    parts.append(list(array))

                if question == 2:
                    p1.extend(parts[0])
                    p2.extend(parts[1])
                elif question == 4:
                    p1.extend(parts[0])
                    p2.extend(parts[1])
                    p3.extend(parts[2])
                    p4.extend(parts[3])
                return p1, p2, p3, p4       
                 
            else:
                print("cant devide")
                continue            
        except ValueError:
            print("Enter valid input")
            continue
