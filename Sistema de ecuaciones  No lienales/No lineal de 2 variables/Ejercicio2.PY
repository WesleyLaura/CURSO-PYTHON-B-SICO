#Ejercicio 2
import numpy as mp  
import matplotlib.pyplot as plt         
from scipy.optimize import fsolve

def ej2(vars ):
    x, y = vars
    return [mp.sin(x) + y**2 - 1, x**2 + y - 2]

#Resolver
sol2 = fsolve(ej2, [1, 1])
print("Ejercicio 2: ", sol2)

#Graficar , estras 3 lineas siguientes son las medidas de nuestra ventana en cual es va mostrar la grafica
x = mp.linspace(-3, 3, 400)
y = mp.linspace(-3, 3, 400)
X, Y = mp.meshgrid(x , y)

plt.contour(X, Y, mp.sin(X) + Y**2 - 1, [0], colors = 'r')
plt.contour(X, Y, X**2 + Y - 2, [0], colors = 'b')
plt.plot(sol2[0], sol2[1], 'go')
plt.title("Ejercicio 2")
plt.xlabel("x"); plt.ylabel("y")
plt.grid(True); plt.show()
