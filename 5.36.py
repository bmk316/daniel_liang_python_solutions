# QUESTION 5.36, Rock, Paper, Scissors

import random

computer_count = 0
player_count = 0

while True:

    text1 = "Computer is: "
    text2 = "You are "
    computer = random.randrange(0, 3, 1)
    player = eval(input("Enter scissor(0), rock(1), paper(2):"))

    if computer < 3:
        if computer == 0:
            text1 += "Scissor"

        elif computer == 1:
            text1 += "Rock"

        else:
            text1 += "Paper"

    if player < 3:

        if player == 0:
            text2 += "Scissor"

        elif player == 1:
            text2 += "Rock"

        else:
            text2 += "Paper"

    if computer == player:
        print(text1 + ".", end=" ")
        print(text2 + " too.", end="\n")
        print("It's a draw, play again!")

    elif (player == computer + 1) or (player == (computer - 2)):
        print(text1 + ".", end=" ")
        print(text2 + ".", end="\n")
        print("You won!")
        player_count += 1
        
    else:
        print(text1 + ".", end=" ")
        print(text2 + ".", end="\n")
        print("You Lost :(")
        computer_count += 1

    print("Computer count is:", computer_count)
    print("Player count is:", player_count)
    print()

    if computer_count > 2 or player_count > 2:
        break

if computer_count > 2:
   print("Computer won more than twice, You Lost the game :(")
elif player_count > 2:
   print("Your winning count is more than 2 games, You won!")
