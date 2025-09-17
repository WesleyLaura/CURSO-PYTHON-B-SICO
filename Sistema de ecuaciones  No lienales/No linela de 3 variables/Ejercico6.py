# EJERCICIO 6 ( SIN USAR FUNCION DEF)

import numpy as mp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

sistema = lambda v :[
    v[0]**2 + v[1] + v[2] - 4,
    v[1]**2 + v[2] + v[0] - 5,
    v[2]**2 + v[0] + v[1] - 6
    
]

sol = fsolve(sistema, [1, 1, 1])
print("Ejercicio 6  - solucion aproximada (x ,y , z) =" , sol)
