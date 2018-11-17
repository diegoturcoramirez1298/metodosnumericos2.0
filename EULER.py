# Metodo de Euler
# y' - 2xy = 0 y(1) =1  y(1.5) = ?
# dy/dx = 2y
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return math.sin(x) + math.log(y)

def euler(y0,x,h,f):
    y = []
    y.append(y0)
    for i in range(1,len(x)):
        y.append( y[i-1] + h*f(x[i-1],y[i-1]) )
    return y

n = 20
a = 0.1
b = 0.05
h = abs(a-b)/(n-1)
x = np.linspace(a,b,n)
y = euler(1,x,h,f)

plt.plot(x,y,'g')
#plt.plot(x,[math.exp(xi) for xi in x],'b')
plt.grid()
