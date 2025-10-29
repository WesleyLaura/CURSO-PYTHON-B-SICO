# METODO DE GAUSS-SEIDEL
import numpy as np 

def gauss_seidel(A, b, tol = 1e-6, max_iter = 100):
    n = len(b)
    x = np.zeros(n)
    for i in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            s = sum(A[i][j]*x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        if np.linalg.norm(x_new - x, ord = np.inf) < tol:
            return x_new
        x = x_new
    return x

# Ejemplo 1
A = np.array([[4, 1], [1, 3]])
b = np.array([15, 10])
print("Solucion Ejercicio 1 (GAUSS - SEIDEL): ", gauss_seidel(A, b))

# Ejemplo 2
A = np.array([[1, 1, -1], [1, 4, 1], [1, 1, 5]])
b = np.array([1, 2, 0])
print("Solucion Ejercicio 2 (GAUSS - SEIDEL): ", gauss_seidel(A, b))        