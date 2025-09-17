import numpy as mp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def ej3(vars ):
    x, y = vars
    return [x**3 - y , x + y**2 - 4]

#Resolver
sol3 = fsolve(ej3, [1, 1])
print("Ejercicio 3: ", sol3)

#Graficar , estras 3 lineas siguientes son las medidas de nuestra ventana en cual es va mostrar la grafica
x = mp.linspace(-3, 3, 400)
y = mp.linspace(-3, 3, 400)
X, Y = mp.meshgrid(x , y)

plt.contour(X, Y, X**3 - Y , [0], colors = 'r')
plt.contour(X, Y,  X + Y**2 - 4, [0], colors = 'b')
plt.plot(sol3[0], sol3[1], 'go')
plt.title("Ejercicio 3")
plt.xlabel("x"); plt.ylabel("y")
plt.grid(True); plt.show()
