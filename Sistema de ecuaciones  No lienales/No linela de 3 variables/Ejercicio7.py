# EJERCICIO 7 ( SIN USAR FUNCION DEF)

import numpy as mp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

sistema = lambda v :[
    mp.exp(v[0]) + v[1] + v[2] - 4,
    v[0] + mp.exp(v[1]) + v[2] - 5,
    v[0] + v[1] + mp.exp(v[2]) - 6
    
]

sol = fsolve(sistema, [1, 1, 1])
print("Ejercicio 7  - solucion aproximada (x ,y , z) =" , sol)
