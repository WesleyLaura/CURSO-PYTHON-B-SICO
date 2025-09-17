# EJERCICIO 8 ( SIN USAR FUNCION DEF)

import numpy as mp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

sistema = lambda v :[
    mp.sin(v[0]) + v[1] + v[2]**2 - 3,
    v[0] + mp.cos(v[1]) + v[2] - 2,
    v[0]**2 + v[1]**2 + v[2] - 4
    
]

sol = fsolve(sistema, [1, 1, 1])
print("Ejercicio 8  - solucion aproximada (x ,y , z) =" , sol)
