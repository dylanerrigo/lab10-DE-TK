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