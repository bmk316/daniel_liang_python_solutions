#QUESTION 4.17, Rock, Paper, Scissors

import random

computer = random.randrange(0,3,1)

player = eval(input("Enter scissor(0), rock(1), paper(2):"))

text1 = "Computer is: "
text2 = "You are "

if computer == 0:
    text1 += "Scissor"

elif computer == 1:
    text1 += "Rock"

elif computer == 2:
    text1 += "Paper"

if player == 0:
    text2 += "Scissor"

elif player == 1:
    text2 += "Rock"

elif player == 2:
    text2 += "Paper"

if computer == player:
    print(text1 + ".", end=" ")
    print(text2 + " too.", end=" ")
    print("It's a draw!")

elif (player == computer + 1) or (player == (computer - 2)):
    print(text1 + ".", end=" ")
    print(text2 + ".", end=" ")
    print("You won!")

else:
    print(text1 + ".", end=" ")
    print(text2 + ".", end=" ")
    print("You Lost :(")