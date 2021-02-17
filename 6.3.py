#PALINDROME NUMBER

def reverse(num):
    temp = num
    rev = 0

    while num > 0:
        rev = rev*10 + num%10
        num = num//10

    return temp == rev


def isPalindrome():
    number = eval(input("Enter the number to check whether it is a palindrome or not: "))

    print(reverse(number))

isPalindrome()