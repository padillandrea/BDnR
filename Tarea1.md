# TP 1 - Python

* Andrea Carolina Padilla Rodríguez | 166605
* Maritrini García Ruiz | 151490
* Marco Antonio Chacón Amaro | 165681
* Víctor Manuel Jiménez González | 165681
---


```python
#Metodos auxiliares
def imprimir_matriz(A):
    for a in A:
        print(a)
    print()
```

## Ejercicio 1

Usando el lenguaje de programación Python, elabora programas para resolver lo planteado en los siguientes incisos:  
1. Desplazar a la izquierda o a la derecha los elementos de una lista (vector).


```python
def desplazar_vector(A, n, k):
    '''
    Desplaza los elementos de una lista k unidades a la izquierda (negativo) o derecha (positivo).

            Parameters:
                    A (list): Una lista
                    n (int): cantidad de elementos en la lista
                    k (int): lugares a dezplazar donde -len(A) <= k <= len (A)

            Returns:
                    A (str): Lista desplazada
    '''

    if not (-n < k < n):
        A[:] = [0 for _ in range(n)]
        return A
    
    # Desplazar derecha
    if k > 0:
        A[k:] = A[:-k]
        A[:k] = [0 for _ in range(k)]
    #Desplazar izquierda
    elif k < 0:
        A[:k] = A[-k:]
        A[k:] = [0 for _ in range(-k)] 
    return A

# Creamos una lista con elelentos del 1 al 10
A = [i + 1 for i in range(10)]
# Unidades a desplazar
k = 4

desplazar_vector(A, len(A), k)
print(A)
```

    [0, 0, 0, 0, 1, 2, 3, 4, 5, 6]


2. Hacer la suma de dos matrices a(m, n) y b(m, n). Los datos pueden darse en la forma que se quiera.


```python
def sumar_matrices(A, B):
    '''
    Suma dos matrices con las mismas dimensiones.

            Parameters:
                    A (list[list]): matriz (m x n)
                    B (list[list]): matriz (m x n)

            Returns:
                    C (list[list]): A + B
    '''
    # Suma haciendo uso de comprensión de listas anidadas (por fila y después por posición)
    C = [[a + b for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]
    return C

# Pruebas
A = [[ a for a in range(3)] for i in range(5)] # Definimos matriz A
B = [[ i * a for a in range(3)] for i in range(5)] # Definimos matriz B
imprimir_matriz(A)
imprimir_matriz(B)

# Mostramos la suma
imprimir_matriz(sumar_matrices(A, B))
```

    [0, 1, 2]
    [0, 1, 2]
    [0, 1, 2]
    [0, 1, 2]
    [0, 1, 2]
    
    [0, 0, 0]
    [0, 1, 2]
    [0, 2, 4]
    [0, 3, 6]
    [0, 4, 8]
    
    [0, 1, 2]
    [0, 2, 4]
    [0, 3, 6]
    [0, 4, 8]
    [0, 5, 10]
    


## Ejercicio 2

Escribe la función `tuplaPares` que reciba una tupla como parámetro y regrese una tupla que
contenga los elementos que se encuentran en una posición par de la tupla dada como parámetro,
comenzando por el primero. Por ejemplo, si recibe `('Yo', 'mi', 'a', 'prueba', 'tupla')`, entonces
`tuplaPares` regresará `('Yo', 'a', 'tupla')`. 


```python
def tuplaPares(tupla):
    '''
    Regresa los elementos pares de un tupla.

            Parameters:
                    tupla (tuple)

            Returns:
                    tupla2 (tuple)
    '''
    # Crea tupla a traves de una comprensión de lista
    return tuple([tupla[e] for e in range(0, len(tupla), 2)])

# Prueba
tupla = ('Yo', 'mi', 'a', 'prueba', 'tupla')
print(tuplaPares(tupla))
```

    ('Yo', 'a', 'tupla')


## Ejercicio 3

Escribe una función `interseccion()` que tome dos listas y devuelva `True` si tienen al menos 1
elemento en común o devuelva `False` en caso contrario. 


```python
def interseccion(listaA, listaB):
    '''
    Verifica si dos listas tienen al menos un elemento en comun.

            Parameters:
                    listaA (list): lista con elementos
                    listaB (list): lista con elementos

            Returns:
                    res (bool): tiene o no elementos en comun
    '''
    
    # Iteramos sobre las dos listas
    for a in listaA:
        for b in listaB:
            # En caso de encontrar el mismo elemento en las listas regresar True
            if a == b:
                return True
    return False

# pruebas
listaA = [e for e in range(10)]
listaB = [e for e in range(9, 14)]
print(listaA)
print(listaB)
print(interseccion(listaA, listaB))
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [9, 10, 11, 12, 13]
    True


## Ejercicio 4

Escribe una función que reciba una cadena y devuelva un diccionario con la cantidad de
apariciones de cada palabra en la cadena. Por ejemplo, si recibe "que día tan lluvioso que hace
hoy", debe devolver: `{'que': 2, 'día': 1, 'tan': 1, 'lluvioso': 1, 'hace': 1, 'hoy': 1}` 


```python
def contar_palabras(frase):
    '''
    Cuenta el número de veces que ocurre cada palabra en una cadena

            Parameters:
                    frase (String): frase en la que se cuentas las palabras

            Returns:
                    ocurrencias (dict): número de ocurrencias por palabra
    '''
    # Almacenar cada palabra de la cadena
    palabras = frase.split()
    ocurrencias = dict()
    
    # Iterar sobre la lista de palabras y contar su frecuencia
    for palabra in palabras:
        ocurrencias[palabra] = ocurrencias.get(palabra, 0) + 1
        
    return ocurrencias

# Pruebas
frase = "que día tan lluvioso que hace hoy"
print(contar_palabras(frase))
```

    {'que': 2, 'día': 1, 'tan': 1, 'lluvioso': 1, 'hace': 1, 'hoy': 1}


## Ejercicio 5

Escribe una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar
y devuelva la cantidad de veces que se observa cada valor que aparece de los dados. 


```python
from random import randint

def numero_combinacion_de_dados(n):
    '''
    Cuenta las combinaciones de dos dados en n lanzamientos

            Parameters:
                    n (int): numero de lanzamiento de dados

            Returns:
                    num_dice_combos (dict): número de ocurrencias por combinación de dado
    '''
    num_dice_combos = dict()
    
    # Tiramos y contamos dados
    for i in range(n):
        c = randint(1, 6), randint(1, 6) # lanzamiento de dados aleatorio
        num_dice_combos[c] = num_dice_combos.get(c, 0) + 1
    return num_dice_combos

counter = numero_combinacion_de_dados(10000)

# Imprimimos las combinaciones en orden
for dice in sorted(counter, reverse = True, key = lambda dice: dice):
    print(dice,":",counter[dice])
```

    (6, 6) : 280
    (6, 5) : 290
    (6, 4) : 294
    (6, 3) : 297
    (6, 2) : 275
    (6, 1) : 237
    (5, 6) : 281
    (5, 5) : 255
    (5, 4) : 262
    (5, 3) : 282
    (5, 2) : 291
    (5, 1) : 279
    (4, 6) : 287
    (4, 5) : 268
    (4, 4) : 273
    (4, 3) : 282
    (4, 2) : 277
    (4, 1) : 258
    (3, 6) : 262
    (3, 5) : 285
    (3, 4) : 305
    (3, 3) : 305
    (3, 2) : 277
    (3, 1) : 321
    (2, 6) : 266
    (2, 5) : 283
    (2, 4) : 284
    (2, 3) : 278
    (2, 2) : 280
    (2, 1) : 258
    (1, 6) : 300
    (1, 5) : 285
    (1, 4) : 233
    (1, 3) : 278
    (1, 2) : 271
    (1, 1) : 261


## Ejercicio 6

Un programa para hacer la multiplicación de dos matrices A(m, n) y B(n, p). Los datos pueden
especificarse explícitamente dentro del programa o ser leídos desde archivo. 


```python
def mult_matrices(A,B):
    '''
    Realiza la multiplicación de dos matrices A(m, n) y B(n, p).

            Parameters:
                    A (list[list]): matriz (m x n)
                    B (list[list]): matriz (n x p)

            Returns:
                    M (list[list]): A * B
    '''
    m=len(A) #filas de A
    n=len(A[0]) #columnas de A, filas de B
    p=len(B[0]) #columnas de B

    M = [[0 for j in range(m)] for x in range(p)]
    try: # Se ejecutará correctamente si las matrices son m x n * n x p
        for fila in range(m):
            for col in range(p):
                #print(M[columna][fila]) - FORMA DE RECORRER LA MATRIZ M
                #DE ARRIBA-ABAJO-IZQUIERDA-DERECHA
                suma = 0
                for h in range(n):
                    suma = suma + A[fila][h]*B[h][col]

                M[col][fila] = suma
        return M
    except Exception:
        return 'La multiplicacion entre matrices debe ser m x n * n x p'
    
A = [[1,3,2,7],[2,4,5,8]]
B = [[1,3,4],[20,40,4],[4,5,4]]
print(mult_matrices(A,B))
C = [[1,3,2],[2,4,5]]
print(mult_matrices(C,B))
```

    La multiplicacion entre matrices debe ser m x n * n x p
    [[69, 102], [133, 191], [24, 44]]


## Ejercicio 7

Un programa que contenga una función que reciba dos cadenas de caracteres, cuente y regrese
la cantidad de veces que aparece la segunda cadena en la primera. Por ejemplo, si la primera
cadena es 'azcbobobegghakl' y la segunda 'bob', entonces la función regresará un dos.  
>El programa deberá imprimir:  
    `Cantidad de veces que bob ocurre es: 2`


```python
from functools import reduce

def ocurrencias_en_una_frase(frase, palabra):
    if len(frase) < len(palabra):
        return -1
    
    contador = 0
    base = 27
    
    funcion_hash = lambda h, c: h * base + ord(c)
    frase_hash = reduce(funcion_hash, frase[:len(palabra)], 0)
    palabra_hash = reduce(funcion_hash, palabra, 0)  
    power_palabra = base**max(len(palabra) - 1, 0)
    
    for i in range(len(palabra), len(frase)):
        
        if frase_hash == palabra_hash and frase[i - len(palabra):i] == palabra:
            contador += 1
        frase_hash -= ord(frase[i - len(palabra)]) * power_palabra
        frase_hash = frase_hash * base + ord(frase[i])
    
    
    if frase_hash == palabra_hash and frase[-len(palabra):] == palabra:
            contador += 1
        
    return contador

frase = 'azcbobobobobobegghbobobaklbob'
palabra = 'bob'
ocurrencias = ocurrencias_en_una_frase(frase, palabra)
print(f"Cantidad de veces que {palabra} ocurre es: {ocurrencias}")
```

    Cantidad de veces que bob ocurre es: 8


# Ejercicio 8

Un programa que lea palabras desde un archivo de texto y cuente cuántas veces aparece cada
palabra distinta. Utiliza un diccionario para resolver el problema. También imprime la cantidad
total de palabras distintas.


```python
def cuenta_palabras(archivo):
    '''
    Cuenta el número de veces que ocurre cada palabra en un archivo de texto

            Parameters:
                    archivo (String): frase en la que se cuentas las palabras

            Returns:
                    dicc (dict): número de ocurrencias por palabra
    '''
    dicc = {}
    # Se abre el archivo
    archivo_lectura = open('texto.txt','r')
    for line in archivo_lectura:
        arre = line.strip().split() # Arreglo de palabras
        for palabra in arre:
            if palabra in dicc:
                dicc[palabra] += 1 # Se suma uno al num. de ocurrencias si la palabra ya existia
            else:
                dicc[palabra] = 1 # Se agrega la palabra al diccionario
    # Se cierra el archivo
    archivo_lectura.close()
    return dicc

diccionario = cuenta_palabras('texto.txt')
print("\n El número de palabras distintas es: ", len(list(diccionario)))

# Imprimimos las palabras por frecuencia, de mayor a menor
for palabra in sorted(diccionario, reverse = True, key = lambda palabra: diccionario[palabra]):
    print("'" + palabra + "':", diccionario[palabra])
```

    
     El número de palabras distintas es:  41
    'que': 3
    'una': 2
    'de': 2
    'zapato': 1
    'rojo': 1
    'Hace': 1
    'anos': 1
    'descubrieron': 1
    'Andromeda': 1
    'no': 1
    'era': 1
    'nebulosa': 1
    'sino': 1
    'galaxia': 1
    'asi': 1
    'lo': 1
    'anuncio': 1
    'The': 1
    'New': 1
    'York': 1
    'Times': 1
    'La': 1
    'nota': 1
    'noviembre': 1
    'relataba': 1
    'el': 1
    'doctor': 1
    'Edwin': 1
    'Powell': 1
    'Hubble': 1
    'considerado': 1
    'padre': 1
    'la': 1
    'cosmologia': 1
    'habia': 1
    'confirmado': 1
    'las': 1
    'nebulosas': 1
    'eran': 1
    'en': 1
    'realidad': 1


## Ejercicio 9

Un programa que contenga una función recursiva que reciba un diccionario y regrese la
cantidad de valores que contiene. Considera que los valores pueden ser de cualquier tipo
(enteros, cadenas, listas, etc.) y tener cualquier tipo de anidamientos (listas de tuplas,
diccionarios con listas, etc.). Prueba tu programa con diferentes tipos de valores. 


```python
def iterable(obj): 
    '''
    Define si un objeto es o no iterable

            Parameters:
                    obj : objeto (lista, diccionario, integer) que se desea verificar

            Returns:
                    boolean : "True" si es iterable
    '''
    try:
        iter(obj)
    except Exception:
        return False
    else:
        return True
    
def numero_de_elementos(elemento):
    '''
    Cuenta el numero de elementos de un diccionario

            Parameters:
                    elemento (dict) : diccionario aninado

            Returns:
                    counter (int) : cantidad de valores que el diccionario contiene
    '''
    counter = 0
    if type(elemento) == type(dict()):
        elemento = elemento.values()
    if iterable(elemento):
        for v in elemento:
            counter += numero_de_elementos(v) # Recursividad
    else:
        return 1
    return counter


# Pruebas
A = {'a':[[[1,2,3] for _ in range(3)] for _ in range(5)], 'b': ['ggg' for _ in range(3)], 'c': (1,2), 'd': 5}
print(A)
print()
print(f"El número de elementos en el diccionario es de {numero_de_elementos(A)}.")
diccionario = {'a': 1, 'b':{'c': 2, 'd': (3, 4)}, 'e': 5, 'f': [6, 7, 8, 9], 'g': [10, {11, 12}], 'h': (13, 14)}
print(diccionario)
print()
print(f"El número de elementos en el diccionario es de {numero_de_elementos(diccionario)}.")
```

    {'a': [[[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]]], 'b': ['ggg', 'ggg', 'ggg'], 'c': (1, 2), 'd': 5}
    
    El número de elementos en el diccionario es de 57.
    {'a': 1, 'b': {'c': 2, 'd': (3, 4)}, 'e': 5, 'f': [6, 7, 8, 9], 'g': [10, {11, 12}], 'h': (13, 14)}
    
    El número de elementos en el diccionario es de 14.


## Ejercicio 10

Un programa que inicialmente lea desde teclado dos cadenas (de 7 caracteres máximo) las
cuales definirán un rango, por lo que la 1ª cadena deberá ser lexicográficamente menor que la
2ª. El programa leerá después n líneas desde un archivo de texto (cada línea de una longitud
máxima de 40 caracteres).  
Los primeros siete caracteres de cada línea del archivo de texto constituirán la "clave" de la
misma. El programa leerá una línea y si su clave está en el rango dado inicialmente, la escribirá
en un archivo de salida. Por ejemplo, si el rango dado es "Jaso" a "Ramos", entonces el archivo
de salida contendrá todas aquellas líneas cuya clave lexicográficamente esté entre estas dos
cadenas. 


```python
archivo_lectura = open('texto.txt','r') #abre el archivo de lectura
archivo_escritura = open('texto_resultado.txt','w') #abre el archivo de escritura
arre = [lin.split("\n") for lin in archivo_lectura] # separa el archivo por lineas
#print(arre)

primer_cad = segunda_cad = ''
while primer_cad >= segunda_cad: #Nos aseguramos de que la cadena 1 sea menor que la cadena 2
    
    primer_cad = input("Ingresa la palabra de max. 7 caracteres con valor del mínimo del rango: ")
    
    while len(primer_cad) > 7: #Nos aseguramos de que sean max. 7 caracteres
        print(primer_cad, "tiene mas de 7 caracteres.")
        primer_cad = input("Ingresa la palabra de max. 7 caracteres con valor del mínimo del rango: ")
        
    segunda_cad = input("Ingresa la palabra de max. 7 caracteres con valor del maximo del rango: ")
    
    while len(segunda_cad) > 7: #Nos aseguramos de que sean max. 7 caracteres
        print(segunda_cad, "tiene mas de 7 caracteres.")
        segunda_cad = input("Ingresa la palabra de max. 7 caracteres con valor del maximo del rango: ") 
        
    if primer_cad >= segunda_cad:
        print("La primera palabra debe ser lexicograficamente menor a la segunda.")

print("Las lineas del texto que lexicograficamente estan entre ", primer_cad, " y ", segunda_cad, " son: ",'\n')

for n in range(0,len(arre),1):
    if  str(primer_cad) < str(arre[n][0][0:7]) < str(segunda_cad): # Verifica que la linea este entre el rango dado
        res = str(arre[n][0][0:40]) + '\n'
        print(res)
        archivo_escritura.write(res) #Graba la linea en el archivo de escritura
```

    Ingresa la palabra de max. 7 caracteres con valor del mínimo del rango: zuricata
    zuricata tiene mas de 7 caracteres.
    Ingresa la palabra de max. 7 caracteres con valor del mínimo del rango: zuricat
    Ingresa la palabra de max. 7 caracteres con valor del maximo del rango: andrea
    La primera palabra debe ser lexicograficamente menor a la segunda.
    Ingresa la palabra de max. 7 caracteres con valor del mínimo del rango: andrea
    Ingresa la palabra de max. 7 caracteres con valor del maximo del rango: zuricat
    Las lineas del texto que lexicograficamente estan entre  andrea  y  zuricat  son: 
    zapato rojo 
    que Andromeda
    no era una nebulosa
    sino una galaxia asi
    lo anuncio The New York Times
    que el doctor Edwin Powell Hubble
    considerado padre de la cosmologia 
    habia confirmado que las 
    nebulosas eran en realidad

