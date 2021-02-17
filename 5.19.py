#Display a pyramid
# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()
num = int(input("Enter the number of rows:"))
for i in range(1, num+1):
    for j in range(1, num-i+1):
        print(end=" ")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i+1):
        print(j, end="")
    print()

# UserInput = int(input("Enter number of lines: "))
#
# NumberOfIterationsinaline = UserInput * 2
#
# for i in range(1, UserInput + 1):
#     s = UserInput + NumberOfIterationsinaline
#     sp = str(s) + "s"
#     print(format(" ", sp), end='')
#     for j in range(i, 0, -1):
#         print(j, end='  ')
#     for j in range(2, i + 1):
#         print(j, end='  ')
#
#     print(format(" ", sp))
#     NumberOfIterationsinaline -= 3