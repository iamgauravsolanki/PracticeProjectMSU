# proj01.py
# CSE 231 Fall 2007
# Programming Project #1
# Created by [Your Name] on [Date]

# Prompt the user for two integer numbers
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

# Calculate the sum, difference, product, integer division, and remainder
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
integer_division_result = num1 // num2  # Integer division
remainder_result = num1 % num2  # Remainder

# Output the results
print("The sum of", num1, "and", num2, "is", sum_result)
print("The difference of", num1, "and", num2, "is", difference_result)
print("The product of", num1, "and", num2, "is", product_result)
print("The integer division of", num1, "by", num2, "is", integer_division_result, "with remainder", remainder_result)
