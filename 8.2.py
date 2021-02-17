#substring of a substrings

def check(str_1, str_2):

    for i in range(len(str_2)):
        if str_2[i] == str_1[0]:
            k = i
            for j in range(0, len(str_1)):
                if str_2[k] == str_1[j]:
                    if j == len(str_1)-1:
                        return True
                    k += 1
                else:
                    break

    return False


def main():

    string_1 = input("Enter the first string:")
    string_2 = input("Enter the second string:")

    result = check(string_1, string_2)

    if result:
        print("String", string_1, "is a substring of string", string_2)

    else:
        print("String", string_1, "is not a substring of string", string_2)

main()





