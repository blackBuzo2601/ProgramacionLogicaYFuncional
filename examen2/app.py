#20760257
#BUZO ZAMORA ELIAN
#PROGRAMACIÓN LÓGICA Y FUNCIONAL | EXAMEN 2

import matplotlib.pyplot as plt

# Función principal: Método de Newton-Raphson usando recursividad y funciones puras
def newton_raphson(f, df, x0, tol=1e-10, max_iter=1000, history=None):
    # history no es mutado: se redefine como una nueva tupla en cada llamada
    if history is None:
        history = ()
    history = history + (x0,)

    fx = f(x0)

    # Condición de convergencia
    if abs(fx) < tol:
        return x0, history
    
    # Si se alcanzó el límite de iteraciones sin converger
    if max_iter == 0:
        raise Exception("Error: se alcanzó el número máximo de iteraciones sin convergencia.")

    return newton_raphson(f, df, x0 - fx / df(x0),
                          tol, max_iter - 1,
                          history)

# Ejemplo de función y derivada
f  = lambda x: x**2 - 2
df = lambda x: 2 * x

# Valor inicial
x0 = 1.0

# Ejecutar método
try:
    raiz, pasos = newton_raphson(f, df, x0)
    print("Raíz aproximada:", raiz)
except Exception as e:
    print(e)

# Graficar iteraciones
plt.plot(range(len(pasos)), pasos, marker='o', linestyle='-', color='blue')
plt.title("Aproximaciones por iteración")
plt.xlabel("Iteración")
plt.ylabel("Valor de x")
plt.grid(True)

# Guardar la gráfica en un archivo
plt.savefig("grafica_iteraciones.png")
