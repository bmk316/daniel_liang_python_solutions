#QUESTION 2.22


print("Current population is: 312,032,486", "\n")

currentpopulation = 312032486
numberOfSecondsInAYear = 365*24*60*60
birthsPerYear = numberOfSecondsInAYear/7
immigrantsPerYear = numberOfSecondsInAYear/45
deathsPerYear = numberOfSecondsInAYear/13

years = eval(input("Enter number of years required to find new population:"))

new_population = (birthsPerYear + immigrantsPerYear - deathsPerYear)*years + currentpopulation

print(f"The population in {years} years is: {new_population:,}")