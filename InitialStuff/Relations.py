from sympy import *
import math

class Triangle:

    def __init__(self):
        #side lengths
        self.a = Symbol('a')
        self.b = Symbol('b')
        self.c = Symbol('c')
        #perimeters
        self.s = Symbol('s')
        self.p = Symbol('p')
        #Angles
        self.A = Symbol('A')
        self.B = Symbol('B')
        self.C = Symbol('C')
        #trig functions
        self.cosA = cos(self.A)
        self.cosB = cos(self.B)
        self.cosC = cos(self.C)
        self.sinA = sin(self.A)
        self.sinB = sin(self.B)
        self.sinC = sin(self.C)
        self.tanA = tan(self.A)
        self.tanB = tan(self.B)
        self.tanC = tan(self.C)
        self.secA = sec(self.A)
        self.secB = sec(self.B)
        self.secC = sec(self.C)
        self.cscA = csc(self.A)
        self.cscB = csc(self.B)
        self.cscC = csc(self.C)
        self.cotA = cot(self.A)
        self.cotB = cot(self.B)
        self.cotC = cot(self.C)
        #Area
        self.T = Symbol("T")


class Relation:

    def __init__(self, lhs, rhs):
        self.LHS = lhs
        self.RHS = rhs

    def display(self):
        print(str(self.LHS), "=", str(self.RHS))

triangle = Triangle()

Reltions = [

    Relation(triangle.T, sqrt((triangle.s) * (triangle.s - triangle.a) * (triangle.s - triangle.b) * (triangle.s - triangle.c))),

    Relation(triangle.tanA, triangle.sinA/triangle.cosA),

    Relation(triangle.tanB, triangle.sinB/triangle.cosB),

    Relation(triangle.tanC, triangle.sinC/triangle.cosC),

    Relation(triangle.secA, 1/triangle.cosA),

    Relation(triangle.secB, 1/triangle.cosB),

    Relation(triangle.secC, 1/triangle.cosC),

]