#Longest Common Prefix

def prefix(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    prefix = ""
    count = 0

    for i in range(0, min(len1, len2)):
        if s1[i] == s2[i]:
            count += 1
            prefix = prefix + s1[i]
        else:
            break
    if count >= 1:
        print("The largest common prefix is - ", prefix)
    else:
        print("Prefix doesn't exist")


def main():
    st1 = input("Enter the first string:")
    st2 = input("Enter the second string:")
    prefix(st1, st2)

main()