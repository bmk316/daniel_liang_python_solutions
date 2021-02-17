#4.21 Zeller's formula to calculate day of the week
# h is the day of the week (0: Saturday, 1: Sunday, 2: Monday, 3: Tuesday 4: Wednesday, 5: Thursday, 6: Friday).
# q is the day of the month.
# m is the month (3: March, 4: April, ..., 12: December). January and February are counted as months 13 and 14 of the previous year.
# j is the century (i.e. year/100).
# k is the year of the century (i.e., year % 100).

import math

saturday = "Saturday"
sunday = "Sunday"
monday = "Monday"
tuesday = "Tuesday"
wednesday = "Wednesday"
thursday = "Thursday"
friday = "Friday"

year = eval(input("Enter the year (e.g., 2007): "))

j = math.floor(year/100)

k = year % 100

m = eval(input("Enter the month: 1-12: ")) #Which month?

q = eval(input("Enter the day of the month: 1-31: ")) #Day of the month

h = (q + math.floor(26 * (m - 2) / 10) + k + math.floor(k / 4) + math.floor(j / 4) + 5 * j) % 7

if m == 1:
    m += 12
    year -= 1
    h = (q + math.floor(26 * (m - 2) / 10) + k + math.floor(k / 4) + math.floor(j / 4) + 5 * j) % 7

if m == 2:
    m += 12
    year -= 1
    h = (q + math.floor(26 * (m - 2) / 10) + k + math.floor(k / 4) + math.floor(j / 4) + 5 * j) % 7

print(h)

if h == 0:
    print("Day of the week is:", saturday)
elif h == 1:
    print("Day of the week is:", sunday)
elif h == 2:
    print("Day of the week is:", monday)
elif h == 3:
    print("Day of the week is:", tuesday)
elif h == 4:
    print("Day of the week is:", wednesday)
elif h == 5:
    print("Day of the week is:", thursday)
elif h == 6:
    print("Day of the week is:", friday)
