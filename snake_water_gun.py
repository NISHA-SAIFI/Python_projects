# snake water gun game
# 1 for snake
# -1 for water
# 0 for gun
import random
# Get the computer's choice randomly
computer=random.choice([1,0,-1])
you_str=input("Enter a snake, water or gun").lower()
you_dic={
    "snake":1,
    "water":-1,
    "gun":0
}
#  user's choice validate or not
if you_str not in you_dic:
    print("Invalid input. Please enter 'snake', 'water', or 'gun'.")
dic_reverse={
    1:"snake",
    -1:"water",
    0:"gun"
}
you=you_dic[you_str]
print(f"You enter {dic_reverse[you]} \n computer chose {dic_reverse[computer]}")
if(computer==you):
    print("It's a draw")
else:
    if(you==1 and computer==-1)or(you==-1 and computer==0)or(you==0 and computer==1):
        print("You win")
    else:
        print("You lose")
