#Guess Game

import random

print("🎯 Number guessing Game")
print("Game Rules : \n game will take a number from the range 1 to 10 and you have to guess and type the number")

target=random.randrange(1,10)


while True:
    guess_input=input("Enter your guess :")

    # validate the input
    if not guess_input.isdigit():
        print("input must be intiger")
        continue

    guess=int(guess_input)
    
    
    #range validate

    if guess<1 or guess>9:
        print("Input is out of range . Please guess between 1 and 10")
        break

    #game logic

    if guess>target:
        print("Too high")
    elif guess<target:
        print("too low")
    else:
        print("Hurrah 🎉 Win 🥳 ")
        break
    









