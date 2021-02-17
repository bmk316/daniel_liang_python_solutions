#Credit Card number validity

def main():
    number = input("Enter the card number:").strip()

    if isValid(number):
        print(number, "is valid")
    else:
        print(number, "is invalid")

# Return true if the card number is valid
def isValid(number):

    return getSize(number) and (number.startswith("4") or number.startswith("5") or
            number.startswith("6") or number.startswith("37")) and \
           (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0

def sumOfDoubleEvenPlace(number):

    sum1 = 0

    for i in range(len(number)-2, -1, -2):
        sum1 += getDigit(int(number[i])*2)

    return sum1


def getDigit(number):

    return number % 10 + (number//10 % 10)

def sumOfOddPlace(number):

    sum1 = 0
    for i in range(len(number)-1,-1,-2):
        sum1 += int(number[i])

    return sum1


def getSize(d):

    if 13 >= len(d) <= 16:
        return True

    return False

main()
# def prefixMatchedNumber(number, d):
#     pass

# def getPrefix(number, k):
#     pass