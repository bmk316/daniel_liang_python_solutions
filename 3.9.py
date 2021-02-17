#QUESTION 3.9
#Financial Application : monetary units

employee_name = input("Enter Employee's name:")
number_of_hours = eval(input("Enter number of hours worked per week:"))
hourly_rate = eval(input("Enter the hourly pay rate:"))
tax_withholding = eval(input("Enter federal tax withholding rate in % equivalent:"))
state_withholding = eval(input("Enter state tax withholding rate in % equivalent:"))

gross_pay = number_of_hours * hourly_rate

deductions_fed = round((tax_withholding * gross_pay),2)
# print(deductions_fed)
deductions_state = round((state_withholding * gross_pay),2)
total_deductions = round((deductions_state + deductions_fed),2)
net_pay = round((gross_pay - total_deductions),2)

print("### EMPLOYEE REPORT ###")
print("Employee's name:", employee_name)
print("Hours worked:", number_of_hours)
print("Pay Rate:$"+str(hourly_rate))
print("Gross Pay:$"+str(gross_pay))
print("Deductions:")
print("\t Federal Withholding (20.0%): $" + str(deductions_fed))
print("\t State Withholding (9.0%): $" + str(deductions_state))
print("\t Total Deduction: $" + str(total_deductions))

print("Net Pay: $" + str(net_pay))




