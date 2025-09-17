#METODO DE GAUSS - JORDAN
import numpy as np 

def gauss_jordan(A, b):
    n = len(b)
    #M = np.hstack([A.astype(float), b.reshape(-1, 1)])
    M = np.hstack([A.astype(float), b ])
    for k in range(n):
        M[k] = M[k] / M[k][k]
        for i in range(n):
            if i != k:
                M[i] = M[i] - M[i][k] * M[k]
                
    return M[:, -1]

#Ejemplo 1
A = np.array([[1, 2], [3, -1]])
b = np.array([[5], [4]]) 
print("Solucion Ejercicio 1 (GAUSS- JORDAN): ", gauss_jordan(A, b))       

#Ejemplo 2
A = np.array([[2, 1, -1], 
              [-3, -1, 2], 
              [-2, 1, -3]])
b = np.array([[5], [4], [6]]) 
print("Solucion Ejercicio 2 (GAUSS- JORDAN): ", gauss_jordan(A, b)) 

#Ejercicio de la clase 
A = np.array([[2, 3, 4], 
              [2, 6, 8], 
              [4, 9,-4]])
b = np.array([[3],[5],[4]]) 
print("Solucion del ejercico de la clase (GAUSS- JORDAN): ", gauss_jordan(A, b))   