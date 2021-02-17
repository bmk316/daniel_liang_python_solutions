import random

first_number = random.randrange(0,100)
second_number = random.randrange(0,100)

answer = eval(input("What is " + str(first_number) + "+" + str(second_number) + "?"))

print(first_number, "+", second_number, "=", answer, "is", first_number + second_number == answer)