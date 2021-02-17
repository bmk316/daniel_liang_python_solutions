#did not submit

def CountOccur(list1):
    temp = [0] * 100

    for num in list1:
        temp[num] += 1

    for i in range(len(temp)):
        if temp[i] > 1:
            print(i, "occurs", temp[i], "times")
        elif temp[i] == 1:
            print(i, "occurs", temp[i], "time")


def main():
    list1 = eval(input("Enter integers between 1 and 100: "))
    CountOccur(list1)


main()

# 10.3 (Count occurrence of numbers) Write a program that reads some integers
# between 1 and 100 and counts the occurrences of each.

n = input("Enter integers between 1 and 100: ")
lst = [int(x) for x in n.split()]
counted = []
for x in lst:
    if x not in counted:
        c = lst.count(x)
        if c > 1:
            print(x, "occurs", c, "times")
        else:
            print(x, "occurs", c, "time")
        counted.append(x)