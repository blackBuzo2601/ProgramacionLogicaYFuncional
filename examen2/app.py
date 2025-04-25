import matplotlib.pyplot as plt

# Función principal: Método de Newton-Raphson usando recursividad y funciones puras
def newton_raphson(f, df, x0, tol=1e-10, max_iter=1000, iteraciones=None):
    if iteraciones is None:
        iteraciones = []
    
    fx = f(x0)
    iteraciones.append(x0)

    if abs(fx) < tol or max_iter == 0:
        return x0, iteraciones

    return newton_raphson(f, df, x0 - fx / df(x0), tol, max_iter - 1, iteraciones)

# Ejemplo de función y derivada
f = lambda x: x**2 - 2
df = lambda x: 2 * x

# Valor inicial
x0 = 1.0

# Ejecutar método
raiz, pasos = newton_raphson(f, df, x0)

print("Raíz aproximada:", raiz)

# Graficar iteraciones
plt.plot(range(len(pasos)), pasos, marker='o', linestyle='-', color='blue')
plt.title("Aproximaciones por iteración")
plt.xlabel("Iteración")
plt.ylabel("Valor de x")
plt.grid(True)

# Guardar la gráfica
plt.savefig("grafica_iteraciones.png")