#Find future dates

today = eval(input("Enter an integer for today's day of the week from 0 - 6, Sunday is 0 and Saturday is 6:"))
elapsed_days = eval(input("Enter the number of days elapsed since today:"))

Sunday = "Sunday"
Monday = "Monday"
Tuesday = "Tuesday"
Wednesday = "Wednesday"
Thursday = "Thursday"
Friday = "Friday"
Saturday = "Saturday"

future_date = (today + elapsed_days) % 7

if today == 0:
    today = Sunday
elif today == 1:
    today = Monday
elif today == 2:
    today = Tuesday
elif today == 3:
    today = Wednesday
elif today == 4:
    today = Thursday
elif today == 5:
    today = Friday
elif today == 6:
    today = Saturday

if future_date == 0:
    future_date = Sunday
elif future_date == 1:
    future_date = Monday
elif future_date == 2:
    future_date = Tuesday
elif future_date == 3:
    future_date = Wednesday
elif future_date == 4:
    future_date = Thursday
elif future_date == 5:
    future_date = Friday
elif future_date == 6:
    future_date = Saturday

print("Today's day is", today, "and the future day is:", future_date)


