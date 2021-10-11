import random

attempt = 0
answer = random.randrange(0, 50)
print(answer)
while attempt < 10:
    try:
        guess = int(input("Enter guessing number here: "))
        if attempt == 9 and guess != answer:
            print("You Loose")
            break
        elif attempt == 9 and guess == answer:
            print("You Win")
            break
        elif guess < answer:
            print("guess is lower then answer")
            attempt += 1
            continue
        elif guess > answer:
            print("guess is greater then answer")
            attempt += 1
            continue
        else:
            print("You Win")
            break
    except ValueError:
        print("Enter valid information!!")
        continue
