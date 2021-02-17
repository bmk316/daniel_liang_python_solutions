# 5.35 Perfect Number
# order = []
for i in range(1, 10000):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s += j
    if s == i:
        # order.append(i)
        print(i, "is a Perfect Number")

# print(order)