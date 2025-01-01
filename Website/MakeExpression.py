from sympy import *
import random

def generate_expression():
    weights = [1, 1, 1, 1, 1, 2, 2, 3]
    terms = [
        (cos(Symbol("A")), 0),
        (cos(Symbol("B")), 0), 
        (cos(Symbol("C")), 0),
        (sin(Symbol("A")), 0),
        (sin(Symbol("B")), 0),
        (sin(Symbol("C")), 0),
        (Symbol("a"), 1),
        (Symbol("b"), 1),
        (Symbol("c"), 1),
        (Symbol("s"), 1),
        (Symbol("r"), 1),
        (Symbol("R"), 1),
        (Symbol("m_A"), 1),
        (Symbol("m_B"), 1),
        (Symbol("m_C"), 1),
        (Symbol("h_A"), 1),
        (Symbol("h_B"), 1),
        (Symbol("h_C"), 1),
        (Symbol("T"), 2)
    ]
    numerator = 1
    denominator = 1
    numerator_n = 0
    denominator_n = 0
    symbol_set = set()
    for _ in range(0, random.randint(0, 3)):
        n = [0, 0, 0, 1, 1, 1, 1, 1, 2][random.randint(0, 8)]
        exp = 0
        for i in range(0, weights[random.randint(0, 7)]):
            if n == 0:
                s = terms[random.randint(0,5)][0]
                symbol_set.add(s)
                exp += s
            elif n == 1:
                s = terms[random.randint(6,17)][0]
                symbol_set.add(s)
                exp += s
            else:
                s = terms[18][0]
                symbol_set.add(s)
                exp += s
        if exp != 0:
            numerator_n += n
            numerator *= exp
    for _ in range(0, random.randint(1, 3)):
        n = [0, 0, 0, 0, 1, 1, 1, 1, 2][random.randint(0, 8)]
        exp = 0
        for i in range(0, weights[random.randint(0, 7)]):
            if n == 0:
                s = terms[random.randint(0,5)][0]
                symbol_set.add(s)
                exp += s
            elif n == 1:
                s = terms[random.randint(6,17)][0]
                symbol_set.add(s)
                exp += s
            else:
                s = terms[18][0]
                symbol_set.add(s)
                exp += s
        if exp != 0:
            denominator_n += n
            denominator *= exp
    
    if denominator == 0:
        return (None, "", "")
    if numerator_n == denominator_n:
        return (numerator/denominator, latex(numerator/denominator), symbol_set)
    else:
        return (None, "", "")