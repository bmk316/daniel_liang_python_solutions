# QUESTION 2.6

number = eval(input("Input number between 0 and 1000, whose integers need to be summed: "))
first_digit = number % 10
print(first_digit)
number_after_extracting_first_digit = number // 10
second_digit = number_after_extracting_first_digit % 10
print(second_digit)
third_digit = number_after_extracting_first_digit // 10
print(third_digit)
print("Sum of digits is: ", int(first_digit+second_digit+third_digit))