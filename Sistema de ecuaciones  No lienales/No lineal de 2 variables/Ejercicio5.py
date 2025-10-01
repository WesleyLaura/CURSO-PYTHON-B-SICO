import numpy as mp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def ej5(vars ):
    x, y = vars
    return [mp.log(x+2) + y - 1, x**2 - y - 2]

#Resolver
sol5 = fsolve(ej5, [1, 1])
print("Ejercicio 5: ", sol5)

#Graficar , estras 3 lineas siguientes son las medidas de nuestra ventana en cual es va mostrar la grafica
x = mp.linspace(-1.9, 3, 400)
y = mp.linspace(-3, 3, 400)
X, Y = mp.meshgrid(x , y)

plt.contour(X, Y,mp.log(X + 2) + Y - 1, [0], colors = 'r')
plt.contour(X, Y,  X**2 - Y - 2 , [0], colors = 'b')
plt.plot(sol5[0], sol5[1], 'go')
plt.title("Ejercicio 5")
plt.xlabel("x"); plt.ylabel("y")
plt.grid(True); plt.show()
