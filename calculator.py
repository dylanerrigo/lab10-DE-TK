#https://github.com/dylanerrigo/lab10-DE-TK.git
#Partner 1: Dylan Errigo
#Partner 2: Tristan Kerr
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def square_root(a):
    try:
        return math.sqrt(a)
    except:
        raise ValueError('Argument cannot be less than zero.')
def hypotenuse(a,b):
    return math.hypot(a,b)
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