#Sistemas de Ecuacieon No lineadles de 2 Variables
# Ejercicio 1: x**2 + y**2 = 4, e**x + y = 1
import numpy as mp 
import matplotlib.pyplot as plot   
from scipy.optimize import fsolve   

def ej1(vars):
    x ,y = vars
    return [x**2 + y**2 - 4, mp.exp(x) + y -1]

#Resolver

sol1 = fsolve(ej1, [0.5, 0.5])
print ("Ejercicio 1 : ", sol1)

#Graficar
x = mp.linspace(-3, 3, 400)
y = mp.linspace(-3, 3, 400)
X, Y = mp.meshgrid(x , y)

plot.contour(X, Y , X**2 + Y**2 - 4, [0], colors = 'r')
plot.contour(X, Y , mp.exp(X) + Y -1, [0], colors = 'b')
plot.plot(sol1[0], sol1[1],'go')
plot.title("Ejercicio 1")
plot.xlabel("x"); plot.ylabel("y")
plot.grid(True); plot.show()