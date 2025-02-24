# @file    HW6.py
# @author  Brayden Davis
# @date    February 23rd 2025
# @brief   This is for homework six.
num1 = input("What is the first number?") #This is to ask what the first input is.
num2 = input("What is the second number?") #This is to ask what the second input is.
sum = int(num1) + int(num2) #This is how it finds the sum.
print("The sum is...")
print(sum) #This is how it prints the sum.
if int(num1) > int(num2): #This is how it finds the difference. It puts the greater number first.
  print("the difference is...")
  difference = int(num1) - int(num2)
else:
  difference = int(num2) - int(num1)
  print("The difference is...")
print(difference) #This is how it prints the difference.
product = int(num1) * int(num2) #This is how it finds the product.
print("The product is...")
print(product) #This is how it prints the product.
quotient = int(num1) / int(num2) #This is how it finds the quotient.
print("The quotient is...")
print(quotient) #This is how it prints the quotient.