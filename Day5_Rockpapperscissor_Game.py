import sys
import random


print("".ljust(20,"-"))

my_choice=int(input("choose rock 💎 press 1 \n choose scissor ✂️ press 2 \n choose paper 🥅 press 3 \n please choose :"))
computer_choice= int(random.choice("123"))

print(f"my choice :{my_choice}")

print(f"computer choice :{computer_choice}")

if my_choice==3 and computer_choice==1:
    print("\n 🎉 you win!")
elif my_choice==2 and computer_choice==3:
    print("\n 🎉 you win!")
elif my_choice==1 and computer_choice==2:
    print("\n 🎉 you win!")
elif my_choice==computer_choice:
    print("\n 🪢 tie!")
    
else :
    print("\n 🐍 computer Win!")

print("".ljust(20,"-"))