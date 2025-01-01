import math
import GetValue
from sympy import *

def categorize(a, b, c):
    categorize = ("", "")
    if a == b == c:
        categorize = ("equilateral", "")
    elif a == b != c or a == c != b or b == c != a:
        categorize = ("isosceles", "")
    elif a != b and b != c and a != c:
        categorize = ("scalene", "")
    if min(a, b, c)**2 + (a + b + c - min(a, b, c) - max(a, b, c))**2 == max(a, b, c)** 2:
        categorize = (categorize[0], "right")
    return categorize


def valid(Symbols_set, expr, i):
    #min_value = math.inf
    #max_value = 0
    satisfies = {"equilateral" : True, "isosceles" : True, "scalene" : True, "right" : True, "" : False}
    for a in range(1, 101):
        for b in range(1, 101):
            for c in range(1, 101):
                if max(a, b, c) >= GetValue.get_value(a, b, c, Symbol("s")):
                    continue
                type = categorize(a, b, c)
                #print(Symbols_set)
                symbol_values = []
                for symbol in Symbols_set:
                    symbol_values.append((symbol, GetValue.get_value(a, b, c, symbol)))
                #print(symbol_values)
                value = expr.subs(symbol_values)
                if value == (Symbol("x")/0).subs([(Symbol("x"),1)]):
                    if i % 2 == 0:
                        return False
                    else:
                        continue
                if i == 0 and value != 1:
                    satisfies[type[0]] = False
                    satisfies[type[1]] = False
                if i == 1 and not(value > 1):
                    satisfies[type[0]] = False
                    satisfies[type[1]] = False
                if i == 2 and not(value < 1):
                    satisfies[type[0]] = False
                    satisfies[type[1]] = False
                if i == 3 and not(value >= 1):
                    satisfies[type[0]] = False
                    satisfies[type[1]] = False
                if i == 4 and not(value <= 1):
                    satisfies[type[0]] = False
                    satisfies[type[1]] = False

                if satisfies["equilateral"] == satisfies["isosceles"] == satisfies["scalene"] == satisfies["right"] == False:
                    return False
    return satisfies