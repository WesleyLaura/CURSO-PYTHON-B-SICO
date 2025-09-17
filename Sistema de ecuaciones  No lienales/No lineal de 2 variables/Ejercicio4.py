import numpy as mp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def ej4(vars ):
    x, y = vars
    return [mp.exp(x) + y - 3, x**2 + y**2 - 5]

#Resolver
sol4 = fsolve(ej4, [1, 1])
print("Ejercicio 4: ", sol4)

#Graficar , estras 3 lineas siguientes son las medidas de nuestra ventana en cual es va mostrar la grafica
x = mp.linspace(-3, 3, 400)
y = mp.linspace(-3, 3, 400)
X, Y = mp.meshgrid(x , y)

plt.contour(X, Y, mp.exp(X) + Y - 3, [0], colors = 'r')
plt.contour(X, Y,  X**2 + Y**2 - 5, [0], colors = 'b')
plt.plot(sol4[0], sol4[1], 'go')
plt.title("Ejercicio 4")
plt.xlabel("x"); plt.ylabel("y")
plt.grid(True); plt.show()
