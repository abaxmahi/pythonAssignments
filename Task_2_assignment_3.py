"""
Docstring for Taskk_2_assignment_3
program using the math module for calculation
Also assuming the log base e
and sine value in radians.
"""
import math as m
number = float(input("Enter the Number: "))

def sq_rt(n):
    if n < 0:
        print("Undefined !! must be greater than 0")
    else:
        return m.sqrt(n)

def logarithm(x):
    if x <= 0:
        print("Undefined !! must be greater than 0")
    else:
        return m.log(x)

def sine(y):
    return m.sin(y)

print(f"Square root : {sq_rt(number)}")
print()
print(f"Logarithm : {logarithm(number)}")
print()
print(f"Sine : {sine(number)}")

