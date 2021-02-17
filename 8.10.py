def decimalToBinary(value):
    bin = ''
    while value > 0:
        if value % 2 == 0:
            bin = bin + '0'
        else:
            bin = bin + '1'
        value = value // 2
    bin = bin[::-1]
    return bin


def main():
    val = eval(input("Enter a decimal: "))
    bin = decimalToBinary(val)
    print(bin)


main()