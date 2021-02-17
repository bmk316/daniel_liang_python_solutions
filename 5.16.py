#GCD - both approached
n1 = eval(input("Enter the first number:"))
n2 = eval(input("Enter the second number:"))

#FIRST approach:
# while k <= n1 and k <= n2:
#     if n1 % k == 0 and n2 % k == 0:
#         gcd = k
#     k += 1
#SECOND approach
if n1 < n2:
    d = n1 #setting one of the numbers as a minimum
else:
    d = n2

while d <= n1 and d <= n2:
    if n1%d == 0 and n2%d == 0:
        break
    d -= 1

print("The GCD of", n1, "and", n2, "is :", d)



