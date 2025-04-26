# 20760257
# BUZO ZAMORA ELIAN
# PROGRAMACIÓN LÓGICA Y FUNCIONAL | EXAMEN 2

import matplotlib.pyplot as plt  # Importamos la librería pyplot de matplotlib para crear gráficos

# Definimos la función principal que implementa el método de Newton-Raphson de forma recursiva y pura
def newton_raphson(funcion, derivada, valor_inicial, tolerancia=1e-10, maximo_iteraciones=1000, historial=None):
    # `historial` llevará registro inmutable de cada valor de x calculado
    # Si es la primera llamada (historial es None), lo inicializamos como una tupla vacía
    if historial is None:
        historial = ()
    # Añadimos el valor actual valor_inicial al historial creando una nueva tupla (no mutamos nada)
    historial = historial + (valor_inicial,)

    # Calculamos el valor de la función en el punto valor_inicial
    valor_funcion = funcion(valor_inicial)

    # 1) Condición de convergencia:
    #    Si |funcion(valor_inicial)| es menor que la tolerancia especificada, consideramos que hemos encontrado
    #    una aproximación suficientemente buena a la raíz.
    if abs(valor_funcion) < tolerancia:
        return valor_inicial, historial  # Devolvemos la raíz aproximada y toda la secuencia de pasos

    # 2) Condición de parada por exceso de iteraciones:
    #    Si hemos agotado el número máximo de llamadas recursivas (maximo_iteraciones llega a 0),
    #    lanzamos un error avisando de que no se alcanzó la convergencia.
    if maximo_iteraciones == 0:
        raise Exception("Error: se alcanzó el número máximo de iteraciones sin convergencia.")

    # 3) Cálculo del siguiente punto usando la fórmula de Newton-Raphson:
    #    siguiente_valor = valor_inicial - funcion(valor_inicial) / derivada(valor_inicial)
    #    Disminuimos maximo_iteraciones en 1 y llamamos recursivamente con el nuevo valor
    siguiente_valor = valor_inicial - valor_funcion / derivada(valor_inicial)
    
    return newton_raphson(
        funcion, derivada,
        siguiente_valor,
        tolerancia,
        maximo_iteraciones - 1,
        historial
    )

# ======================
# Definición de la prueba
# ======================

# Definimos la función de prueba: f(x) = x^2 - 2, cuya raíz buscamos (√2 ≈ 1.4142)
funcion_prueba  = lambda x: x**2 - 2

# Definimos su derivada: f'(x) = 2 * x
derivada_prueba = lambda x: 2 * x

# Escogemos un valor inicial razonable cerca de la raíz esperada
valor_inicial = 1.0

# Ejecutamos el método guardando la raíz y el historial de aproximaciones
try:
    raiz_aproximada, historial_pasos = newton_raphson(funcion_prueba, derivada_prueba, valor_inicial)
    # Mostramos en consola la aproximación final de la raíz
    print("Raíz aproximada:", raiz_aproximada)
except Exception as error:
    # Si ocurre un error (no converge), mostramos el mensaje correspondiente
    print(error)

# =========================
# Graficación de la evolución
# =========================

# 'historial_pasos' contiene la tupla con todos los valores de x en cada iteración:
# e.g. (x0, x1, x2, ...)
# range(len(historial_pasos)) crea una secuencia 0,1,2,... para el eje de iteraciones
plt.plot(
    range(len(historial_pasos)),  # eje X: número de iteración
    historial_pasos,              # eje Y: valor de x_n en esa iteración
    marker='o',                   # marca cada punto con un círculo
    linestyle='-',                # une los puntos con líneas
    color='blue'                  # color azul para la línea
)

# Añadimos título y etiquetas para que el gráfico sea claro
plt.title("Aproximaciones por iteración")
plt.xlabel("Iteración")
plt.ylabel("Valor de x")
plt.grid(True)  # Activamos la cuadrícula para facilitar la lectura de los valores

# Guardamos el gráfico como una imagen PNG en el directorio actual
plt.savefig("grafica_iteraciones.png")
