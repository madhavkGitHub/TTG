from sympy import *
import time
a = Symbol("a")
b = Symbol("b")
c = Symbol("c")
s = Symbol("s")
expr1  = (a + b) / c
expr2 = 2 * s / c - 1
expr3 = s / c


op_1 = time.time()
for i in range(1,101):
    for j in range(1,101):
        for k in range(1, 101):
            semi = (i + j + k)/2
            if max(i, j, k) >= semi:
                continue
            value = expr3.subs({s : semi, c : k})
print(time.time() - op_1)

var_3 = time.time()
for i in range(1,101):
    for j in range(1,101):
        for k in range(1, 101):
            semi = (i + j + k)/2
            if max(i, j, k) >= semi:
                continue
            value = expr1.subs({a : i, b : j, c : k})
print(time.time() - var_3)

var_2 = time.time()
for i in range(1,101):
    for j in range(1,101):
        for k in range(1, 101):
            semi = (i + j + k)/2
            if max(i, j, k) >= semi:
                continue
            value = expr2.subs({s : semi, c : k})
print(time.time() - var_2)
