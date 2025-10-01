# Ejercicio 1: x^3 - x - 2 = 0
import math
import matplotlib.pyplot as plot
import numpy as mp

def f(x): 
    return x**3 - x - 2 

def bisection_iteration(f ,a, b ,tol= 1e-8, maxit = 100):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("No cambio de signo en [a,b]")
    rows=[]
    for k in range (1,maxit + 1):
        r = (a + b) / 2
        fr = f(r)
        rows.append((k, a, b, r, f(r)))
        if abs(fr) < tol or (b - a) / 2 < tol: break
        if fa * fr < 0:
            b, fb = r, fr
        else:
            a, fa = r, fr
    return rows

def secant_iteration(f, x0, x1, tol = 1e-8, maxit = 100):
    rows = []
    for k in range(1, maxit + 1):
        fx0, fx1 = f(x0), f(x1)
        if fx1 == fx0 : raise ZeroDivisionError("Denominador cero")
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        fx2 = f(x2)
        rows.append((k, x0, x1, x2, f(x2)))
        if abs(fx2) < tol or abs(fx2) < tol: break
        X0, x1 = x1, x2
    return rows

a,b = 1.0, 2.0
bis = bisection_iteration(f, a, b)
sec = secant_iteration(f, a, b)

print("Biseccion (primeras 6 iter / ultima):")
for row in bis[:6]: print(row)
print("...", bis[-1])
print("\nSecante (todas iter mostradas):")
for row in sec: print(row)
print("\n Resultado final:")
print("Biseccion:", bis[-1][3], "iter=", bis[-1][0])
print("Secante:", sec[-1][3], "iter=", sec[-1][0])
#VAMOS A  MOSTRARA LA GRAFICA DE LA FUNCION


# Graficar f(x) y las raíces aproximadas
x = mp.linspace(-3, 3, 400)
y = f(x)

# Últimas aproximaciones
root_bis = bis[-1][3]
root_sec = sec[-1][3]

plot.axhline(0, color="black", linewidth=0.8)  # eje X
plot.plot(x, y, label="f(x) = x^3 - x - 2")
plot.plot([a, b], [f(a), f(b)], "go", label="Extremos [a,b]")

# Raíces aproximadas
plot.plot(root_bis, f(root_bis), "ro", label="Raíz Bisección")
plot.plot(root_sec, f(root_sec), "bx", markersize=10, label="Raíz Secante")

plot.title("Ejercicio 1: f(x) = x^3 - x - 2")
plot.xlabel("x")
plot.ylabel("f(x)")
plot.legend()
plot.grid(True)
plot.show()







    