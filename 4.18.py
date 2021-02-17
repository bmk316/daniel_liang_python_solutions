#4.18, Financial Currency exchange - US Dollars to RMB

correct_rate = 6.81
exchange_rate = eval(input("Enter the exchange rate from US dollars to Chinese Renminbi (RMB):"))
print()

while exchange_rate == correct_rate:

    choice = eval(input("Enter 0 to convert dollars to RMB and 1 for vice-versa:"))

    if choice == 0:

        dollar_amount = eval(input("Enter the Dollar amount:"))

        calc1 = round(dollar_amount* exchange_rate,2)
        print("$"+str(dollar_amount)+" is "+str(calc1) + ".")

    elif choice == 1:
        rmb_amount = float(input("Enter the RMB amount:"))

        calc2 = round(rmb_amount / exchange_rate, 2)
        print(str(rmb_amount) + " yuan" + " is " + str(calc2) + ".")

print("You have entered the wrong exchange rate. Please enter 6.81")