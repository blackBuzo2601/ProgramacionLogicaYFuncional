#EJEMPLO DE RECURSIVIDAD
#INTEGRANTES:
#BUZO ZAMORA ELIAN
#RAMIREZ SANTIAGO ELEAZAR 
#VILLAVICENCIO ARCE MANUEL GERARDO
#DAVID CALEB ROMERO BARRERAS


def factorial(n): 
    if n == 0 or n == 1:  
        return 1 #termina la recursión
    else:
        return n * factorial(n - 1)

numero = 5
resultado = factorial(numero) #5*4...*3...*2...*1
print(f"El factorial de {numero} es {resultado}")
