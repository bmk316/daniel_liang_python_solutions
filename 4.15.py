import random

lottery = random.randrange(100,1000,1)
guess = eval(input("Enter your lottery pick(3 digits):"))

lotteryDigit1 = lottery % 10
lotteryDigit2 = (lottery // 10) % 10
lotteryDigit3 = lottery // 100

guessDigit1 = guess % 10
guessDigit2 = (guess // 100) % 10
guessDigit3 = guess // 100

print("The lottery number is:", lottery)

if guess == lottery:
    print("You win $10,000!")

elif guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit2 and guessDigit3 == lotteryDigit3:
    print("Match all digits, you win $3,000!")

elif guessDigit1 == lotteryDigit1 \
     or guessDigit1 == lotteryDigit2\
     or guessDigit1 == lotteryDigit3\
     or guessDigit2 == lotteryDigit1\
     or guessDigit2 == lotteryDigit2\
     or guessDigit2 == lotteryDigit3\
     or guessDigit3 == lotteryDigit1\
     or guessDigit3 == lotteryDigit2 \
     or guessDigit3 == lotteryDigit3:

    print("You matched one digit, you win $1,000!")

else:
    print("Sorry,no match :( UGH!")




