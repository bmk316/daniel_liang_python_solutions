#SORT THREE NUMBERS


def displaySortedNumbers(n1,n2,n3):

    a1 = max(n1,n2,n3)
    a3 = min(n1,n2,n3)
    a2 = (n1+n2+n3) - a1 - a3

    return a3,a2,a1


def testProgram():
    num1, num2, num3 = eval(input("Enter the 3 numbers to be sorted:"))
    print(displaySortedNumbers(num1, num2, num3))

testProgram()