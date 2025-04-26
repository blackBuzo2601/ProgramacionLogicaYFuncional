# 20760257
# BUZO ZAMORA ELIAN
# PROGRAMACIÓN LÓGICA Y FUNCIONAL | EXAMEN 2

import matplotlib.pyplot as plt  #Importamos la librería matplotlib para poder graficar los resultados

#1e-10 => 0.0000000001 
#Como queremos que la raíz aproximada sea muy precisa, entre más pequeña es la tolerancia
#más exacta será la raíz que obtendremos. 
#la tolerancia se usa como condición para detener la recursión cuando la diferencia entre 
#f(x) y 0 es lo suficientemente pequeña (es decir, cuando estamos demasiado cerca de la raíz).
def newton_raphson(funcion, derivada, valor_inicial, tolerancia=1e-10, maximo_iteraciones=1000, historial=None):
    #Si es la primera vez que se llama a la función, 'historial' será None (nulo),
    #así que lo inicializamos como una tupla vacía para empezar a guardar los pasos desde cero.
    if historial is None:
        historial = ()

    #Tomamos una copia de la tupla que teníamos construida en historial y le agregamos el nuevo valor.
    #Esto se hace así porque las tuplas son inmutables, o sea, no podemos modificarlas directamente.
    #Entonces lo que hacemos es crear una nueva tupla que incluye la anterior + el nuevo valor.
    historial = historial + (valor_inicial,)

    #Evaluamos la función en el punto actual (valor_inicial) para ver qué tan cerca estamos de la raíz.
    valor_funcion = funcion(valor_inicial)

    #Verificamos si el valor absoluto de f(x) es menor que la tolerancia que definimos.
    #Si esto se cumple, significa que estamos lo suficientemente cerca de 0,
    #lo que se traduce que ya encontramos la raíz con un buen valor de precisión
    if abs(valor_funcion) < tolerancia:
        #Devolvemos el valor actual (la raíz aproximada) y el historial de todos los valores que calculamos.
        return valor_inicial, historial

    #Si ya usamos todas las iteraciones permitidas y aún no llegamos a una raíz,
    #detenemos la ejecución con un error
    if maximo_iteraciones == 0:
        raise Exception("Error: se alcanzó el número máximo de iteraciones sin convergencia.")

    #Aplicamos la fórmula del método de Newton-Raphson para encontrar el siguiente valor de x:
    #   xn+1 = xn - f(xn) / f'(xn)
    #Aquí se calcula ese siguiente valor a partir del punto actual.
    siguiente_valor = valor_inicial - valor_funcion / derivada(valor_inicial)

    #Llamamos recursivamente a la misma función con el nuevo valor calculado
    #y restamos 1 a maximo_iteraciones, tambien retornamos el historial para
    #seguir guardando los pasos recorridos
    #El historial también se pasa para seguir guardando todos los pasos recorridos.
    return newton_raphson(
        funcion, derivada,
        siguiente_valor,
        tolerancia,
        maximo_iteraciones - 1,
        historial
    )

# Esta es la funcion de prueba: f(x) = x^2 - 2. Sabemos que su raíz es la 
#raíz cuadrada de 2 ==>1.4142...
funcion_prueba  = lambda x: x**2 - 2

#Definimos su derivada que sería: f'(x) = 2x. Defnir la derivada 
#es necesario porque Newton-Raphson usa la derivada para avanzar en0 cada paso.
derivada_prueba = lambda x: 2 * x

#Definimos un punto de partida cercano a la raíz esperada.
#Puede ser cualquier número real, pero si está muy lejos, puede tardar más en converger.
valor_inicial = 1.0


#Guardamos dos cosas:
#raiz_aproximada: el valor final donde creemos que está la raíz
#historial_pasos: una tupla con todos los valores de x que calculamos
try:
    raiz_aproximada, historial_pasos = newton_raphson(funcion_prueba, derivada_prueba, valor_inicial)
    print("Raíz aproximada:", raiz_aproximada)

# Si por alguna razón se llegó al límite de iteraciones sin encontrar una buena aproximación,
# mostramos el mensaje de error correspondiente.
except Exception as error:
    print(error)

plt.plot(
    range(len(historial_pasos)), 
    historial_pasos,             
    marker='o',                   
    linestyle='-',                
    color='blue'                 
)


plt.title("Aproximaciones por iteración")  
plt.xlabel("Iteración")                    
plt.ylabel("Valor de x")                   
plt.grid(True)                            


plt.savefig("grafica.png")    
