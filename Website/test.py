from sympy import *
import math

angle_A = cos(Symbol("A"))

angle_B = Symbol("B")

print(angle_A.subs([(cos(Symbol("A")), 1/2)]))
print((math.cos(angle_B.subs([(angle_B, math.pi/3)]))))