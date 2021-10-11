import random

count = 0
phone_list = []
while count < 100:
    List_of_index = [555, 595, 558, 577]
    generated_random_numbers = []
    for i in range(1, 7):
        generated_random_numbers.append(random.randint(0, 9))
        number = ""
        for num in generated_random_numbers:
            number += str(num)
    phone_Number = str(random.choice(List_of_index)) + str(number)
    phone_list.append(phone_Number)
    count += 1

    with open("numbers.txt", 'w') as file:
        for number in phone_list:
            file.writelines(number + "\n")

with open("numbers.txt", "r") as file:
    a = 0
    b = 0
    c = 0
    d = 0
    data = file.readlines()

    for each in data:
        if each[0:3] == "555":
            a += 1
        elif each[0:3] == "595":
            b += 1
        elif each[0:3] == "558":
            c += 1
        elif each[0:3] == "577":
            d += 1
    Dict = {"555": a, "595": b, "558": c, "577": d}

    sort = sorted(Dict.items())
    print("Most common index: " + str(sort[-1][0]) + " Used " + str(sort[-1][1]) + " times")
