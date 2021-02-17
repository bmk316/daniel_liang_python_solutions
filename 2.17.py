#QUESTION 2.17
# HEALTH APPLICATION

weight_pounds = eval(input("Enter your weight in pounds: "))
height_inches = eval(input("Enter your weight in pounds: "))

pounds_to_kilos = weight_pounds * 0.45359237
inches_to_metres = height_inches * 0.0254

print("BMI is:", pounds_to_kilos/(inches_to_metres**2))