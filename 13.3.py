def main():
    text_file = input("Enter a filename: ").strip()
    readfile = open(text_file, "r")

    stringFile = readfile.read()
    words = stringFile.split()

    scores = [eval(x) for x in words]
    total = len(scores)

    sum1 = 0
    for i in scores:
        sum1 += i

    print("Total scores is: ", sum1)
    print("Average is: ", sum1/total)

    readfile.close()


main()