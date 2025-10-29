"""
Laboratorio Practica 6: Métodos Multivariables (Punto Fijo y Newton - Raphson
modificado)
Incluye:
- 4 ejercicios con Punto Fijo multivariable
- 4 ejercicios con Newton - Raphson modificado
"""
import numpy as np
import pandas as pd
from math import sin, cos, sqrt, exp
# --------------------------------------------------------------
# MODELAMIENTO COMPUTACIONAL PARA INGENIERIA - Métodos numéricos
# --------------------------------------------------------------
def punto_fijo_multivariable(g, x0, tol=1e-8, maxiter=100):
    """
    Método de punto fijo multivariable: x_{k+1} = g(x_k)
    g: función que recibe vector y devuelve vector (numpy array)
    x0: vector inicial
    """
    x = x0.astype(float).copy()
    history = []
    for k in range(1, maxiter+1):
        x_new = np.asarray(g(x))
        err = np.linalg.norm(x_new - x, ord=np.inf)
        history.append((k, x.copy(), x_new.copy(), err))
        x = x_new
        if err < tol:
            break
    return x, err, k, history

def newton_modificado(f, J, x0, tol=1e-8, maxiter=50):
    """
    Newton-Raphson modificado (Jacobiano congelado en x0):
    - Evalúa J0 = J(x0) una vez y lo usa para todas las iteraciones.
    - Cada iteración resuelve J0 * delta = -f(x_k)
    """
    x = x0.astype(float).copy()
    J0 = np.asarray(J(x0))
    history = []
    try:
        for k in range(1, maxiter+1):
            fx = np.asarray(f(x))
            delta = np.linalg.solve(J0, -fx)
            x_new = x + delta
            err = np.linalg.norm(delta, ord=np.inf)
            resnorm = np.linalg.norm(fx, ord=2)
            history.append((k, x.copy(), delta.copy(), err, resnorm))
            x = x_new
            if err < tol and resnorm < tol:
                break
        return x, err, k, history
    except Exception as e:
        return None, str(e), 0, history

def mostrar_historial_puntofijo(history, names=None):
    rows = []
    for k, x_old, x_new, err in history:
        row = {"iter": k}
        if names is None:
            for i, val in enumerate(x_new):
                row[f"x{i}"] = val
        else:
            for i, name in enumerate(names):
                row[name] = x_new[i]
        row["||x_{k+1}-x_k||_inf"] = err
        rows.append(row)
    return pd.DataFrame(rows)

def mostrar_historial_newton(history, names=None):
    rows = []
    for k, x_old, delta, err, resnorm in history:
        row = {"iter": k}
        if names is None:
            for i, val in enumerate(x_old):
                row[f"x{i}"] = val
        else:
            for i, name in enumerate(names):
                row[name] = x_old[i]
        for i, d in enumerate(delta):
            row[f"delta{i}"] = d
        row["||delta||_inf"] = err
        row["||f(x)||_2"] = resnorm
        rows.append(row)
    return pd.DataFrame(rows)

# ---------------------------
# EJERCICIOS DE PUNTO FIJO
# ---------------------------
# Ejercicio PF1: x = cos(y), y = sin(x)
def g1(v):
    x, y = v
    return np.array([cos(y), sin(x)])
x0_1 = np.array([0.5, 0.5])

# Ejercicio PF2: x = sqrt((1+y)/2), y = sqrt((1+x)/2)
def g2(v):
    x, y = v
    return np.array([sqrt((1+y)/2), sqrt((1+x)/2)])
x0_2 = np.array([0.5, 0.5])

# Ejercicio PF3: x = (sin(y)+1)/2, y = (cos(x)+1)/2
def g3(v):
    x, y = v
    return np.array([(sin(y)+1)/2, (cos(x)+1)/2])
x0_3 = np.array([0.3, 0.3])

# Ejercicio PF4: sistema 3 variables
def g4(v):
    x, y, z = v
    return np.array([(cos(y*z)+1)/2, (sin(x)+1)/3, (x*y + 1)/4])
x0_4 = np.array([0.2, 0.2, 0.2])
# Ejercicio PF5: sistema 3 variables modificado
def g5(v):
    x,y,z = v
    return np.array([(cos(y*z)+1)/3, (sin(x)+1)/4, (x*y + 1)/5])
x0_5 = np.array([0.2,0.2,0.2])
# Ejercicio PF6: sistema 3 variables simétrico
def g6(v):
    x,y,z = v
    return np.array([sqrt((1+y+z)/4), sqrt((1+x+z)/4), sqrt((1+x+y)/4)])
x0_6 = np.array([0.5,0.5,0.5])

# ---------------------------
# EJERCICIOS NEWTON–RAPHSON MODIFICADO
# ---------------------------
# Ejercicio NRM1: f1 = x^2+y^2-4, f2 = exp(x)+y-1
def f_nr1(v):
    x, y = v
    return np.array([x**2 + y**2 - 4, exp(x) + y - 1])
def J_nr1(v):
    x, y = v
    return np.array([[2*x, 2*y],[exp(x), 1.0]])
x0_nr1 = np.array([1.0, 1.7])

# Ejercicio NRM2: sistema 3 variables
def f_nr2(v):
    x, y, z = v
    return np.array([x + y + z - 3, x**2 + y**2 + z**2 - 5, exp(x) + y - z - 1])
def J_nr2(v):
    x, y, z = v
    return np.array([[1,1,1],[2*x,2*y,2*z],[exp(x),1,-1]])
x0_nr2 = np.array([1.0, 0.5, 1.7]) # cuando a 0.1 para ver si eso es el error

# Ejercicio NRM3: f1 = x^2 - y -1, f2 = y^2 - x -1
def f_nr3(v):
    x, y = v
    return np.array([x**2 - y - 1, y**2 - x - 1])
def J_nr3(v):
    x, y = v
    return np.array([[2*x, -1],[-1, 2*y]])
x0_nr3 = np.array([1.5, 1.5])

# Ejercicio NRM4: f1 = sin(x)+y-1, f2 = x+cos(y)-0.5
def f_nr4(v):
    x, y = v
    return np.array([sin(x) + y - 1, x + cos(y) - 0.5])
def J_nr4(v):
    x, y = v
    return np.array([[cos(x), 1], [1, -sin(y)]])
x0_nr4 = np.array([0.5, 0.5])

# ---------------------------
# MAIN (PRINCIPAL): resolver todos los ejercicios
# ---------------------------
if __name__ == "__main__":
    print("===== PUNTO FIJO =====")
    for i, (g, x0, name) in enumerate([
        (g1,x0_1,"PF1: cos/sen"),
        (g2,x0_2,"PF2: sqrt-symmetric"),
        (g3,x0_3,"PF3: sen/cos scaled"),
        (g4,x0_4,"PF4: 3-variable"),
        (g5,x0_5,"EJERCICIO 9"),
        (g6,x0_6,"EJERCICIO 10")]):
        
        sol, err, iters, hist = punto_fijo_multivariable(g, x0, tol=1e-10, maxiter=500)
        df = mostrar_historial_puntofijo(hist)
        print(f"{name}: solución = {sol}, iteraciones = {iters}, error final = {err}")
        print(df.tail(), "\n")

    print("===== NEWTON–RAPHSON MODIFICADO =====")
    for i, (f, J, x0, name) in enumerate([
        (f_nr1,J_nr1,x0_nr1,"NRM1: circle+exp"),
        (f_nr2,J_nr2,x0_nr2,"NRM2: 3-var"),
        (f_nr3,J_nr3,x0_nr3,"NRM3: symmetric quad"),
        (f_nr4,J_nr4,x0_nr4,"NRM4: sin/cos mix")]):
        sol, err, iters, hist = newton_modificado(f, J, x0, tol=1e-10, maxiter=50)
        if sol is None:
            print(f"{name}: error -> {err}")
        else:
            df = mostrar_historial_newton(hist)
            print(f"{name}: solución = {sol}, iteraciones = {iters}, error final = {err}")
            print(df.tail(), "\n")
