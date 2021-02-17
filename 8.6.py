def count(str1):
    c = 0
    for i in range(len(str1)):
        if str1[i].isalpha() > 0:
            c += 1
    return c


def main():
    string = input("Enter your string to be counted:").lower()

    result = count(string)

    print("The numbers of letters in the string is:", count(string))

main()