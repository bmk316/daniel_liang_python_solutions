#QUESTION 3.11
#REVERSE a four digit number

number = eval(input("Enter the four digit number to be reverse: "))

rev = 0
while number >0:
    rev = (rev*10) + number % 10
    number = number//10

print("Reverse of the number is:",rev)