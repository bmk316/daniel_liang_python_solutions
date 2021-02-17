def isSorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False

    return True


def main():
    list_sort = input("Enter the list: ").split(",")

    result = isSorted(list_sort)

    if result:
        print("List is already sorted")
    else:
        print("List is not sorted")

main()