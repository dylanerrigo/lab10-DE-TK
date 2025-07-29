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
    if b==0:
        raise ValueError('Argument/antilogarithm cannot be zero')
    if a<=1:
        raise ValueError('Base cannot be zero.')
    return math.log(b,a)