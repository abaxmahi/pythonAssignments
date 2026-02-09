"""
Program to calculate the factorial of a number
using the  recursion
"""

def fact(n): 
    if n <= 0:
        return 1
    else:
        return n * fact(n-1)
number = int(input("Enter the Number to find it's Factorial: "))
print(f"Factorial of {number} is : {fact(number)}")