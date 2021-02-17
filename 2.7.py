#QUESTION 2.7 #find number of years and days

#365 days = 1 year | 1 day = 24 hours | 1 hour = 60 minutes | 1 minute = 60 seconds

import math
numberOfMinutesInaYear = 365*24*60

minutes = eval(input("Enter the minutes you wish to convert into years and days:"))

years = math.trunc(minutes / numberOfMinutesInaYear)
remaining_minutes = minutes % numberOfMinutesInaYear
days = math.trunc(remaining_minutes / 1440)

print(str(minutes) + " minutes is approximately " + str(years) + " years and " + str(days) + " days.")