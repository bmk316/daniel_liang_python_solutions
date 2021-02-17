import urllib.request


def main():
    readfile = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Lincoln.txt")
    strings = readfile.read()
    print("The number of words in the file is " + str(len(strings.split())))


main()