from sympy import *
import matplotlib.pyplot as plt
import numpy as np

x = [1950,1960,1970,1980,1990,2000]
y = [123.5,131.2,150.7,141.7,203.2,240.5]

pL = ''
for k in range(len(y)):
    pL += str(y[k]) +'*'
    Lxk = 1
    for i in range(len(x)):
        if (i == k):
            continue
        pL += '(x - %f)*'%(x[i])
        Lxk *= (x[k]-x[i])
    pL = pL[:-1]
    pL += '/%f+'%(Lxk)
pL = pL[:-1]

expr = sympify(pL)
#expr = expand(expr)
print(expand(expr))
plt.plot(x,y,'go')

x2 = np.linspace(1950,2000,2010)
x = symbols('x')
y2 = [expr.subs(x,xi) for xi in x2]
plt.plot(x2,y2)
plt.grid()
#El resultado del polinomio de interpolacion radica por inspección entre 140 y 1960
