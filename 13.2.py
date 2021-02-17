def main():
    text_file = input("Enter a filename: ").strip()
    readfile = open(text_file, "r")

    stringFile = readfile.read()
    word = stringFile.split()
    sum1 = 0
    for i in word:
        sum1 += len(i)
    print(str(sum1) + " characters")
    print(str(len(stringFile.split())) + " words")
    print(str(len(stringFile.split('\n'))) + " lines")

    readfile.close()


main()