#EJEMPLO DE LISTA ENLAZADA
#INTEGRANTES:
#BUZO ZAMORA ELIAN
#RAMIREZ SANTIAGO ELEAZAR 
#VILLAVICENCIO ARCE MANUEL GERARDO
#DAVID CALEB ROMERO BARRERAS

def crear_nodo(valor):
    return {
        'valor': valor,
        'siguiente': None  
    }
#retornamos un diccionario (equivalente a un objeto en JS)

#Inicializamos la cabeza y cola en NONE
cabeza = None
cola = None

#Usamos global porque queremos modificar nuestras variables globales dentro de esta función.
def agregar_nodo(valor):
    global cabeza, cola
    nuevo_nodo = crear_nodo(valor)  
    
    if cabeza is None:  #Aquí entra el flujo la primera vez que creamos un nodo.
        cabeza = nuevo_nodo  #Almacena la dirección en memoria del primer nodo.
        cola = nuevo_nodo  #igual almacena la direccion en memoria del primer nodo
    else: #a partir del segundo nodo que creemos, entra a este flujo
    
        cola['siguiente'] = nuevo_nodo 
        #cola anteriormente guardaba la REFERENCIA EN MEMORIA DEL NODO ANTERIOR, cada nodo
        #creado tiene la propiedad "siguiente"=null. Hacemos que su propiedad siguiente tenga
        #una REFERENCIA DE LA MEMORIA donde está creado el nuevo nodo.
        cola = nuevo_nodo  #cola ahora guarda la REFERENCIA EN MEMORIA del nuevo nodo


def ver_lista():
    actual = cabeza  #guardamos la referencia en memoria del nodo "cabeza".
    valores = []

    while actual:  #mientras que actual contenga algo (No es NONE)
        valores.append(actual['valor']) #agregamos al final del arreglo valores el contenido
        #de "valor" del nodo actual.
        actual = actual['siguiente']  #actual ahora almacena la referencia en memoria
        #de lo que hay en "siguiente" del nodo actual (puede ser la referencia en memoria
        #del siguiente nodo o NULL si es el ultimo nodo)

    print("Mostrando lista:")
    print(valores)

agregar_nodo(1)
agregar_nodo(2)
agregar_nodo(3)
agregar_nodo(4)
agregar_nodo(5)
agregar_nodo(10)
ver_lista()

