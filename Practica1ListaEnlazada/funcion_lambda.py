#EJEMPLO DE FUNCION LAMBDA
#INTEGRANTES:
#BUZO ZAMORA ELIAN
#RAMIREZ SANTIAGO ELEAZAR 
#VILLAVICENCIO ARCE MANUEL GERARDO
#DAVID CALEB ROMERO BARRERAS

#Función lambda (anónima.) Cuadrado=almacena nuestra función anónima. Así que
#para llamarla, debemos escribirla como si llamaramos a una función.
cuadrado = lambda x: x ** 2

numero = int(input("Ingresa un número para calcular su cuadrado: "))
print(f"El cuadrado de {numero} es {cuadrado(numero)}")