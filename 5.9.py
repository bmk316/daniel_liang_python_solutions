#Financial application : compute future tuition

tuition = 10000
rate = 0.05
four_years = 0.0

for i in range(14):
    tuition += tuition * 0.05

    if i == 9:
        print(f"Tuition in 10 years is: {tuition :,.2f}")


    if i == 10 or i == 11 or i == 12 or i == 13:
        four_years += tuition

print(f"Total cost of 4 years of tuition, starting 10 years from now is: {four_years :,.2f}")
