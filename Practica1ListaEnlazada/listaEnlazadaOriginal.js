
/*TAREA 1
BUZO ZAMORA ELIAN
20760257
EJEMPLO DE LISTA ENLAZADA EN JAVASCRIPT

Las listas enlazadas son una estructura de datos dinámica
que consisten en secuencias de nodos. Cada nodo tiene dos partes importantes:
1. Datos: La información que se guarda en dicho nodo.
2. Puntero: Una referencia al siguiente nodo en la secuencia.

Otros datos importantes de las listas enlazadas:
CABEZA (el primer nodo de la lista enlazada.): Este es el punto de entrada a la lista, 
porque no podemos acceder a otros nodos sin comenzar por el inicio de la lista.
COLA (El ultimo nodo de la lista enlazada): En una 
lista enlazada simple, el puntero de la cola apunta a
NULL, lo que indica que es el final de la lista.

IMPORTANTE: Si nosotros queremos acceder a un nodo en especifico,
no podemos acceder a él directamente indicando la posicion de éste
como lo hacemos con un array (array[posicion]). En cambio
en las listas enlazadas ocupamos recorrer nodo tras nodo secuencialmente
para llegar al nodo que deseamos.
*/

//Esta funcion va a crear nodos, de acuerdo al parametro "valor" que pasemos al llamarla.
function crearNodo(valor){
    return{ //retorna un objeto con dos propiedades 
        valor: valor,  //el parametro que pasemos a la función (valor), se asigna al "valor" pero del objeto
        siguiente: null //es nulo, puesto que a medida que agregamos otro nodo, se va volviendo el siguiente nodo.
    };
}

//INICIALIZAMOS VARIABLES
let cabeza=null;
let cola=null;

//Funcion para agregar nodos en la posicion siguiente del nodo anterior (si ya se ha creado el primer nodo.)
function agregarNodo(valor){
    const nuevoNodo=crearNodo(valor); //llama a la funcion crearNodo pasandole el mismo parámetro (valor) que
    //pasamos a esta función y nuevoNodo tiene la referencia del objeto creado.
    
    //EN JS, cuando un objeto es CONST, signifca que solo sus propiedades pueden mutar (cambiar).
    //pero no podemos por ejemplo, a esa variable, asignarle  otro tipo de dato.
    
    if(cabeza==null){ //Esto se cumple la primera vez que se agrega un nodo, puesto que cabeza inicialmente es null
        cabeza=nuevoNodo; //cabeza almacena el PRIMER nodo (objeto) que creamos.
        cola=nuevoNodo; //la variable "cola" tambien almacena el objeto del nodo creado.
        
        //JSON.stringify
    }else{
        
        //este bloque de Else, entra cuando creamos el segundo nodo, pues 'cabeza' ha dejado de ser nulo, por que se creó el primer nodo.
        cola.siguiente=nuevoNodo; /*Esta "cola" es del objeto del nodo creado anter-
        iormente. Es decir, por ejemplo cuando creamos el primer Nodo, dicho objeto se esta
        guadando en 'cola'. Dicha 'cola' tiene una propiedad 'siguiente', que era NULL.
        Dicha propiedad la hemos cambiado para que almacene el objeto del nuevoNodo
        Despues del segundo nodo, almacena el objeto del tercero, cuarto nodo y asi sucesivamente...
        */
        cola=nuevoNodo; //esta linea cambia la referencia para que apunte al siguiente nodo.
    }
}

//Mostrar todos los valores de la lista
function verLista(){
    let actual=cabeza; //almacenamos el objeto cabeza en "actual".
    const valores=[]; //inicializamos un arreglo SIN NADA.

    //cuando no ponemos ninguna condicion en un while y solo colocamos una variable, significa que 
    while(actual){ //esto significa: mientras que actual no sea ni NULL ni UNDEFINED.
        valores.push(actual.valor); //metemos al arreglo valores lo que hay en la propiedad VALOR de nuestro objeto (objeto almacenado en cabeza)
        actual=actual.siguiente; //actual, almacena lo que hay en la propiedad SIGUIENTE del objeto.
        //Ese siguiente, sería otro objeto, y así sucesivamente.
    }

    console.log("Mostrando lista:\n"+valores.join('-')); //Usamos join() para mostrar todos los elementos del array valores.
}




agregarNodo(1);
agregarNodo(2);
agregarNodo(3);
verLista();



