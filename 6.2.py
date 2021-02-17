def sumDigits(n):

    s = 0
    while n != 0:
        s += n % 10
        n = n//10   
    return s
    # s = 0
    # for i in str(n):
    #     s += int(i)
    # return s


def main():
    number = eval(input("Enter number whose digits has to be summed:"))

    print("The sum of the digits is:", sumDigits(number))

main()