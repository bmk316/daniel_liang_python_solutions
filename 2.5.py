#QUESTION 2.5

sub_total, gratuity = eval(input("Enter the Sub total and Gratuity rate: "))
Total = (gratuity*sub_total)/100+sub_total
print("The Gratuity is ", gratuity,"% and the Sub Total is", int(Total*100)/100)