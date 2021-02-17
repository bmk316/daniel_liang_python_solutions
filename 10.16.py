def bubblesort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

list1 = [4,3,2,1]
a = print(bubblesort(list1))