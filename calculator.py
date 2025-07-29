"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass
import math
def div(a,b):
    if a==0:
        raise ValueError('Divisor cannot be zero.')
    return b/a
def log(a,b):
    if b<=0:
        raise ValueError('Argument/antilogarithm cannot be less than or equal to zero.')
    if a==1 or a<=0:
        raise ValueError('Base cannot be 1 or equal to or less than zero.')
    return math.log(b,a)

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(a, b):
    # log base a of b
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive")
    return math.log(b, a)

def exp(a, b):
    return a ** b
