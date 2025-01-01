import sympy
from sympy import *


def getPastInequalities():
    signs = ["=", ">", "<", ">=", "<="]
    sign_to_latex = {"=" : "= 1", ">" : "> 1", "<": "< 1", ">=": "\\geq 1", "<=" : "\\leq 1"}
    f = open("results\\expressions.txt", "r")
    v = (open("results\\valid_times.txt", "r")).readlines()
    i = (open("results\\invalid_times.txt", "r")).readlines()
    valid = 0
    invalid = 0
    equations = []
    for l in f.readlines():
        eq = l.strip()
        type = eq[:eq.index(':')]
        if type == "valid":
            type = eq[eq.index("["):]
            print(type)
            eq = eq[:eq.index("[")]
        ineq = eq[eq.index(':') + 2:]
        index = -1
        if ineq.count("<=") == 1:
            index = 4
        elif ineq.count(">=") == 1:
            index = 3
        elif ineq.count("<") == 1:
            index = 2
        elif ineq.count(">") == 1:
            index = 1
        elif ineq.count("=") == 1:
            index = 0
        
        sign = signs[index]
        expr = sympy.sympify(ineq[:ineq.index(sign)-1])
        latex = "$" + sympy.latex(expr) + " " + sign_to_latex[sign] + "$"
        time = 0
        if type != "invalid":
            time = v[valid].strip()
            valid += 1
        else:
            time = i[invalid].strip()
            invalid += 1
        equations.append((type, expr, latex, time, index, makeSymbolSet(expr)))
    return equations 

def makeSymbolSet(expr):
    atoms = expr.atoms()
    symbol_set = set()
    for a in atoms:
        try:
            print(int(a))
        except:
            if str(a) != "A" and str(a) != "B" and str(a) != "C":
                symbol_set.add(a)
            elif str(a) == "A":
                symbol_set.add(cos(Symbol("A")))
                symbol_set.add(sin(Symbol("A")))
            elif str(a) == "B":
                symbol_set.add(cos(Symbol("B")))
                symbol_set.add(sin(Symbol("B")))
            elif str(a) == "C":
                symbol_set.add(cos(Symbol("C")))
                symbol_set.add(sin(Symbol("C")))
    return symbol_set


def parseNewTheorem(text):
    signs = ["=", ">", "<", ">=", "<="]
    index = -1
    if text.count("<=") == 1:
        index = 4
    elif text.count(">=") == 1:
        index = 3
    elif text.count("<") == 1:
        index = 2
    elif text.count(">") == 1:
        index = 1
    elif text.count("=") == 1:
        index = 0
    text = text[:text.index(signs[index])]
    expr = sympy.sympify(text)
    symbol_set = makeSymbolSet(expr)
    return (expr, symbol_set, index)

