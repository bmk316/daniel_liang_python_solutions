#PALINDROMIC PRIME FUNCTION - QUESTION 6.24

def reverse(number):
    temp = number
    rev = 0

    while number > 0:
        digit = number % 10
        rev = rev*10 + digit
        number = number//10

    if temp == rev:
        return True


def isPrime(number):
    divisor = 2
    while divisor <= number/2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True #number is prime

#DISPLAY FUNCTION


def printNumberofPrimes(numberOfPrimes):
    numberOfPrimes = 1000
    number_of_primes_per_line = 10

    count = 0
    number = 2

    while number < numberOfPrimes:
        if isPrime(number):

            if reverse(number):

                print(number, end=" ")
                count += 1
                if count % number_of_primes_per_line == 0:
                    print()

        number += 1

#MAIN FUNCTION

def main():
    print("First 100 palindromic prime numbers are")
    printNumberofPrimes(1000)

main()
