# METODO ITERATIVO DE JACOBI
import numpy as np    

def jacobi(A, b, tol=1e-6, max_iter=100):
    n = len(b)
    x = np.zeros(n)
    
    for _ in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        if np.linalg.norm(x_new - x, ord = np.inf) < tol:
            return x_new
        x = x_new
    return x

# Ejemplo 1
A = np.array([[10, 1], [1, 10]])
b = np.array([9, 20])
print("Solucion Ejercicio 1 (JACOBI): ", jacobi(A, b))

# Ejemplo 2
A = np.array([[4, -1, 1], [1, 5, -1], [2, 1, 6]])
b = np.array([7, -8, 6])
print("Solucion Ejercicio 2 (JACOBI): ", jacobi(A, b))
