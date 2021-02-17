#Question 11

#365 days = 1 year | 1 day = 24 hours | 1 hour = 60 minutes | 1 minute = 60 seconds
#7 seconds = 1 birth (+) | 13 seconds = 1 death (-) | 45 seconds (+) = 1 immigrant

print ("QUESTION 11", "\n")
print("Current population is: 312,032,486", "\n")
currentpopulation = 312032486

numberOfSecondsInAYear = 365*24*60*60

birthsPerYear = numberOfSecondsInAYear//7
print('Births Per Year is (7 seconds = 1 birth):', int(birthsPerYear))

deathsPerYear = numberOfSecondsInAYear//13
print('Deaths Per Year is (13 seconds = 1 death:', int(deathsPerYear))

immigrantsPerYear = numberOfSecondsInAYear // 45
print("Immigrants Per Year is (45 seconds = 1 immigrant): ", int(immigrantsPerYear))

population_per_year = birthsPerYear - deathsPerYear + immigrantsPerYear
print(f"Population per year is: {population_per_year:,}")

first_year = currentpopulation + (1 * population_per_year)
second_year = currentpopulation + (2 * population_per_year)
third_year = currentpopulation + (3 * population_per_year)
fourth_year = currentpopulation + (4 * population_per_year)
fifth_year = currentpopulation + (5 * population_per_year)

print(f"Population after first year: {first_year:,}")
print(f"Population after second year: {second_year:,}")
print(f"Population after third year: {third_year:,}")
print(f"Population after fourth year: {fourth_year:,}")
print(f"Population after fifth year: {fifth_year:,}", "\n")