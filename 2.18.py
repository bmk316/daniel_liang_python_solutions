#QUESTION 2.18
import time

offset_time = eval(input("Enter time zone offset: "))
total_seconds = time.time()
print("Total seconds is:", int(total_seconds))
current_second = total_seconds % 60
total_minutes = total_seconds //60
current_minute = total_minutes % 60
total_hours = total_minutes // 60
current_hour = (total_hours % 60) + offset_time

print("Current time is :-",int(current_hour),"HRS", ":", int(current_minute),"MINS", ":", int(current_second),"SECONDS")