def sortedList(list):

    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] < list[j]:
                list[j], list[i] = list[i],list[j]

    return list

def main():

    list1 = list(eval(input("Enter some numbers separated by commas for list1: ")))
    list2 = list(eval(input("Enter some numbers separated by commas for list2: ")))

    finallist = list1 + list2

    sortedlList = sortedList(finallist)

    print("The new merged sorted list is:", sortedlList)

main()

