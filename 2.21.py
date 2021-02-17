#QUESTION 2.21
# Financial Application - Compound value

monthly_amount = eval(input("Enter the monthly amount:"))
monthly_interest_rate = 0.05/12 #hard-coded at 5%
accountValue = 0.0

for i in range (6):
    accountValue = (accountValue + monthly_amount)*(1+monthly_interest_rate)

print("After 6 months, the account value will be", accountValue)
