import math
from sympy import *

x = Symbol("x")
y = Symbol("y")

expr = x/y
v = expr.subs([(x, 1), (y, 0)])
print(v == (x/0).subs([(x,1)]))



