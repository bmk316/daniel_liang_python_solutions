# Game: pick a card. Write a program that simulates picking a card from a deck of
# 52 cards. Your program should display the rank (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# Jack, Queen, King) and suit (Clubs, Diamonds, Hearts, Spades) of the card.

import random

rank = random.randint(1,13)

suit = random.randint(1,4)

if rank==1:
    rank1 = "Ace"
elif rank == 2:
    rank1 = 2
elif rank ==3:
    rank1 = 3
elif rank == 4:
    rank1 = 4
elif rank ==5:
    rank1 = 5
elif rank == 6:
    rank1 = 6
elif rank ==7 :
    rank1 = 7
elif rank == 8:
    rank1 =8
elif rank == 9:
    rank1 = 9
elif rank == 10:
    rank1 = 10
elif rank == 11:
    rank1 = "Jack"
elif rank == 12:
    rank1 = "Queen"
elif rank == 13:
    rank1 = "King"

if suit == 1:
    suit1 = "Clubs"
elif suit ==2:
    suit1 = "Diamonds"
elif suit == 3:
    suit1 = "Hearts"
else:
    suit1 = "Spades"

print("The card you picked is the", rank1, "of", suit1)


