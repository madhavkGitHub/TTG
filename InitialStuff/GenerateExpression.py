import math
from sympy import *
import random
import matplotlib.pyplot as plt

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
    quantities = {
        Symbol("a") : a,
        Symbol("b") : b,
        Symbol("c") : c,
        Symbol("s") : semiperimeter(a, b, c),
        Symbol("T") : area(a, b, c),
        cos(Symbol("A")) : math.cos(angle_A(a, b, c)),
        cos(Symbol("B")) : math.cos(angle_B(a, b, c)),
        cos(Symbol("C")) : math.cos(angle_C(a, b, c)),
        sin(Symbol("A")) : math.sin(angle_A(a, b, c)),
        sin(Symbol("B")) : math.sin(angle_B(a, b, c)),
        sin(Symbol("C")) : math.sin(angle_C(a, b, c)),
        Symbol("m_A") : median_A(a, b, c),
        Symbol("m_B") : median_B(a, b, c),
        Symbol("m_C") : median_C(a, b, c),
        Symbol("h_A") : height_A(a, b, c),
        Symbol("h_B") : height_B(a, b, c),
        Symbol("h_C") : height_C(a, b, c),
        Symbol("r") : inradius(a, b, c),
        Symbol("R") : circumradius(a, b, c)
    }
    return quantities[symbol]

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
        return ("", "", "")
    if numerator_n == denominator_n:
        return (numerator/denominator, latex(numerator/denominator), symbol_set)
    else:
        return ("", "", "")

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


def valid(Symboles_set, expr, i):
    min_value = math.inf
    max_value = 0
    satisfies = {"equilateral" : True, "isosceles" : True, "scalene" : True, "right" : True, "" : False}
    for a in range(1, 101):
        for b in range(1, 101):
            for c in range(1, 101):
                if max(a, b, c) >= semiperimeter(a, b, c):
                    continue
                type = categorize(a, b, c)
                #print(Symboles_set)
                symbol_values = []
                for symbol in Symboles_set:
                    symbol_values.append((symbol, get_value(a, b, c, symbol)))
                #print(symbol_values)
                value = expr.subs(symbol_values)
                
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
             
                
        
def main():
    counter = 0
    expr = ""
    while True:
        expr, latex, symbol_set = generate_expression()
        if expr != "":
            inequality = ["= 1", "> 1", "< 1", ">= 1", "<= 1"]
            i = random.randint(0, 4)
            print(inequality[i])
            print(expr)
            print(latex)
            satisfies = valid(symbol_set, expr, i)
            if satisfies != False:
                latex += " " + inequality[i]
                print(latex)
                print(satisfies)
                make_img("$" + latex + "$")
                break
            
        


def make_img(latex_expression):
    fig = plt.figure(figsize=(3, 0.5))  # Dimensions of figsize are in inches
    text = fig.text(
        x=0.5,  # x-coordinate to place the text
        y=0.5,  # y-coordinate to place the text
        s=latex_expression,
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=16,
    )
    plt.savefig("equations/equation.png")
main()