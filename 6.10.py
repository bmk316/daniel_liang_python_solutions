#PRIME FUNCTION
def isPrime(number):
    divisor = 2
    while divisor <= number/2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True #number is prime

#DISPLAY FUNCTION
def printNumberofPrimes(numberOfPrimes):
    number_of_primes = 10000
    number_of_primes_per_line = 10

    count = 0
    number = 2

    while count < number_of_primes:
        if isPrime(number):
            count += 1

            print(number, end=" ")
            if count % number_of_primes_per_line == 0:
                print()

        number += 1

#MAIN FUNCTION

def main():
    print("First 10,000 prime numbers are")
    printNumberofPrimes(10000)

main()

