year = eval(input("Enter a year:"))
first_day = eval(input("Enter first day of the year:"))

number_days_in_a_month = 0
month = 1

for month in range(1, 13):
    if month == 1:
        print("January 1", year, "is", end=" ")
        number_days_in_a_month = 31

    elif month == 2:

        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            number_days_in_a_month = 29
        else:
            number_days_in_a_month = 28

        print("February 1", year, "is", end=" ")

    elif month == 3:
        number_days_in_a_month = 31
        print("March 1", year, "is", end=" ")

    elif month == 4:
        number_days_in_a_month = 30
        print("April 1", year, "is", end=" ")

    elif month == 5:
        number_days_in_a_month = 31
        print("May 1", year,"is", end=" ")

    elif month == 6:
        number_days_in_a_month = 30
        print("June 1", year,"is", end=" ")

    elif month == 7:
        number_days_in_a_month = 31
        print("July 1", year,"is", end=" ")

    elif month == 8:
        number_days_in_a_month = 31
        print("August 1", year,"is", end=" ")

    elif month == 9:
        number_days_in_a_month = 30
        print("September 1", year,"is", end=" ")

    elif month == 10:
        number_days_in_a_month = 31
        print("October 1", year,"is", end=" ")

    elif month == 11:
        number_days_in_a_month = 30
        print("November 1", year,"is", end=" ")

    elif month == 12:
        number_days_in_a_month = 31
        print("December 1", year,"is", end=" ")

    if first_day == 0:
        day = "Sunday"
    elif first_day == 1:
        day = "Monday"
    elif first_day == 2:
        day = "Tuesday"
    elif first_day == 3:
        day = "Wednesday"
    elif first_day == 4:
        day = "Thursday"
    elif first_day == 5:
        day = "Friday"
    elif first_day == 6:
        day = "Saturday"

    first_day = (first_day + number_days_in_a_month) % 7

    print(day)





