import random

my_list = ["hanzo", 20, "rabbit", "penguin", 40]

answer = random.choice(my_list)
print("Choose your answer from this Options: ")

for option in my_list:
    print(option, end=' ')
print("\n") 


guess = input("Enter your guess here: ")
if guess.isdigit():
    if answer == int(guess):
        print("you Win!")
    else:
        print("You Loose!!")
else:
    if answer == guess:
        print("You Win!")
    else:
        print("You Loose")
