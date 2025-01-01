import math
from sympy import *

def semiperimeter(a, b, c):
    return (a + b + c) / 2

def area(a, b, c):
    s = semiperimeter(a, b, c)
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def angle_A(a, b, c):
    return math.acos((b**2 + c**2 - a**2)/(2 * b * c))

def angle_B(a, b, c):
    return math.acos((a**2 + c**2 - b**2)/(2 * a * c))
    
def angle_C(a, b, c):
    return math.acos((a**2 + b**2 - c**2)/(2 * a * b))

def median_A(a, b, c):
    return math.sqrt((a/2)**2 + c**2 + - 2 * (a/2) * c * math.cos(angle_B(a, b, c)))

def median_B(a, b, c):
    return math.sqrt((b/2)**2 + a**2 + - 2 * (b/2) * a * math.cos(angle_C(a, b, c)))

def median_C(a, b, c):
    return math.sqrt((c/2)**2 + b**2 + - 2 * (c/2) * b * math.cos(angle_A(a, b, c)))

def height_A(a, b, c):
    return 2 * area(a, b, c) / a

def height_B(a, b, c):
    return 2 * area(a, b, c) / b

def height_C(a, b, c):
    return 2 * area(a, b, c) / c

def angle_bisector_a(a, b, c):
    x = (a * c / (c + b))
    return math.sqrt(x**2 + c**2 - 2 * x * c * math.cos(angle_B(a, b, c)))

def angle_bisector_b(a, b, c):
    x = (b * a / (a + c))
    return math.sqrt(x**2 + a**2 - 2 * x * a * math.cos(angle_C(a, b, c)))

def angle_bisector_c(a, b, c):
    x = (c * b / (a + b))
    return math.sqrt(x**2 + b**2 - 2 * x * b * math.cos(angle_A(a, b, c)))

def inradius(a, b, c):
    return area(a, b, c)/semiperimeter(a, b, c)

def circumradius(a, b, c):
    return (a * b * c)/(4 * area(a, b, c))

def get_value(a, b, c, symbol):
    if symbol == Symbol("a"):
        return a
    if symbol == Symbol("b"):
        return b
    if symbol == Symbol("c"):
        return c
    
    if symbol == Symbol("s"):
        return semiperimeter(a, b, c)
    if symbol == Symbol("T"):
        return area(a, b, c)
    
    if symbol == cos(Symbol("A")):
        return math.cos(angle_A(a, b, c))
    if symbol == cos(Symbol("B")):
        return math.cos(angle_B(a, b, c))
    if symbol == cos(Symbol("C")):
        return math.cos(angle_C(a, b, c))
    if symbol == sin(Symbol("A")):
        return math.sin(angle_A(a, b, c))
    if symbol == sin(Symbol("B")):
        return math.sin(angle_B(a, b, c))
    if symbol == sin(Symbol("C")):
        return math.sin(angle_C(a, b, c))
    
    
    if symbol == Symbol("m_A"):
        return median_A(a, b, c)
    if symbol == Symbol("m_B"):
        return median_B(a, b, c)
    if symbol == Symbol("m_C"):
        return median_C(a, b, c)
    
    if symbol == Symbol("h_A"):
        return height_A(a, b, c)
    if symbol == Symbol("h_B"):
        return height_B(a, b, c)
    if symbol == Symbol("h_C"):
        return height_C(a, b, c)
    
    if symbol == Symbol("r"):
        return inradius(a, b, c)
    if symbol == Symbol("R"):
        return circumradius(a, b, c)