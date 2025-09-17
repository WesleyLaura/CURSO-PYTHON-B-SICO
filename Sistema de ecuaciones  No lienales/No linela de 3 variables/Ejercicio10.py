# EJERCICIO 10 ( SIN USAR FUNCION DEF)

import numpy as mp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

sistema = lambda v :[
    v[0]**2 + v[1] - 1,
    v[1]**2 + v[2] - 2,
    v[0] + v[2]**2 - 3    
]

sol = fsolve(sistema, [1, 1, 1])
print("Ejercicio 10  - solucion aproximada (x ,y , z) =" , sol)
