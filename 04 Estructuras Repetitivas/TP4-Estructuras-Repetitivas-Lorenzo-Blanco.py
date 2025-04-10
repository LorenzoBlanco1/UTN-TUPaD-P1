import random
import statistics
#----------------------------------------------------------------------------
# Ejercicio 1:
# Crea un programa que imprima en pantalla todos los números enteros desde 0 
# hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando 
# un número por línea.
print(' 1 - Primeros 100 numeros enteros de 0 a 100 de manera creciente. ')
# Estructura repetitiva que sirve para repetir 100 veces la muestra de un numero.
for numero in range(0, 101, 1):
    # Se imprime por pantalla cada numero que toma la variable de iteracion.
    print(f'Numero {numero}')

#----------------------------------------------------------------------------
# Ejercicio 2:
# Desarrolla un programa que solicite al usuario un número entero y 
# determine la cantidad de dígitos que contiene.
print(' 2 - Cantidad de digitos de un numero a ingresar.')
# Se pide al usuario ingresar por teclado un numero.
numero = int(input('Ingrese un numero entero: '))
contador_digitos = 0
# Estructura repetitiva que sirve para dividir sucesivamente por 10 el numero 
# y sumar 1 en el contador de digitos en cada iteracion. 
for i in range(0, numero, 1):
    # Estructura condicional que verifica que el numero sea mayor que cero.
    if numero > 0:
        # Aumenta el contador de digitos
        contador_digitos += 1
        # Se divide el numero por 10 de manera entera para llegar a 0. 
        numero = numero // 10
# Se imprime por pantalla la cantidad de digitos del numero ingresado.
print(f'La cantidad de digitos del numero {numero} es: {contador_digitos}')

#----------------------------------------------------------------------------

# Ejercicio 3:
# Escribe un programa que sume todos los números enteros comprendidos 
# entre dos valores dados por el usuario, excluyendo esos dos valores
print(' 3 - Sumar todos los numeros comprendidos entre 2 numeros a ingrear.')
# Se pide al usuario ingresar por teclado dos numeros.
valor1 = int(input('Ingrese el valor menor: '))
valor2 = int(input('Ingrese el valor menor: '))
sumatoria = 0
# Estructura Condicional para saber si el primer numero es mayor o menor 
# que el segundo.
if valor1 < valor2:
    # Estructura repetitiva para recorrer y sumar cada numero comprendido 
    # entre 2 numeros ingresados.
    for i in range(valor1+1, valor2, 1):
        # Se acumula el valor del iterador en la variable sumatoria.
        sumatoria += i
elif valor1 > valor2:
    for i in range(valor2+1, valor1, 1):
        # Se acumula el valor del iterador en la variable sumatoria.
        sumatoria += i
# Se imprime por pantalla los valores ingresados y la sumatoria de los 
# numero comprendidos entre los mismos. 
print(f'La sumatoria de los numeros entre {valor1} y {valor2} es: {sumatoria}')

#----------------------------------------------------------------------------

# Ejercicio 4:
# Elabora un programa que permita al usuario ingresar números enteros 
# y los sume en secuencia. El programa debe detenerse y mostrar el total
# acumulado cuando el usuario ingrese un 0.
print(' 4 - Sumar numeros ingresados por el usuario hasta que se ingrese el 0.')
# Se pide al usuario ingresar por tecaldo un numero entero.
numero_4 = int(input('Ingrese un numero entero: '))
sumatoria1 = 0
# Estructura repetitiva de permanencia que asegura que el primer 
# numero no es el valor de corte. 
while numero_4 == 0:
    # Se imprime por pantala un mensaje indicando que el primer valor ingresado
    # no puede ser el de corte. 
    print('Se ha ingresado como primer numero la opcion de salida. ')
    # Se pide al usuario ingresar por tecaldo un numero entero.
    # Este numero es el siguiente que evalua la estructura de repeticion.
    numero_4 = int(input('Ingrese un numero entero: '))
# Estructura repetitiva que suma el numero ingresado a a sumatoria 
# y se ingresa el siguiente numero. 
while numero_4 != 0:
    # Se acumula el valor del numero ingresado.
    sumatoria1 = sumatoria1 + numero_4
    numero_4 = int(input('Ingrese un numero entero: '))
# Se imprime por pantalla el valor de la sumatoria. 
print(f'La sumatoria de los numeros enteros ingresados es: {sumatoria1}')

#----------------------------------------------------------------------------

# Ejercicio 5: 
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 
# 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron 
# necesarios para acertar el número.
print(' 5 - Adivinar un numero aleatorio entre 0 y 9.')
# Se asigna un valor aleatorio a la variable utilizando el modulo random.
numero_aleatorio = random.randint(0, 9)
# Se inicializa el contador de intentos en 1 porque minimamente se tiene 
# que ingresar un numero para acertar.
contador_intentos = 1
# Se pide al usuario que ingrese por teclado un numero entero. 
intento = int(input('Ingresar numero: '))
# Estructura Repetitiva de permanencia para saber cuando el usuario acierta.
while intento != numero_aleatorio:
    # Se imprime por pantalla un mensaje que indica que fallo el intento. 
    print('Ha fallado, vuelva a intentar.')
    # Se aumenta en 1 el contador de intentos por cada iteracion del ciclo.
    contador_intentos += 1
    # Se pide al usuario que ingrese por teclado un numero (intento)
    intento = int(input('Ingresar numero: '))
# Estructura condicional para verificar que el ultimo numero ingresado es el correcto. 
if intento == numero_aleatorio:
    # Se imprime por pantalla elm numero aleatorio y la cantidad de intentos.
    print(f'perfecto, ha acertado el numero aleatorio en {contador_intentos} intentos.') 

#----------------------------------------------------------------------------

#Ejercicio 6:
# Desarrolla un programa que imprima en pantalla todos los números 
# pares comprendidos entre 0 y 100, en orden decreciente.
print(' 6 - Numeros pares entre 0 y 100 en orden decreciente.')
# Estructura repetitiva cuya variable de iteracion toma valores del 100 al 0 
# de manera decreciente con paso 2
for numero in range(100, -1, -2):
    # Estructura condicional (opcional) para verificar que el valor del 
    # iterador es par.
    if numero % 2 == 0:
        # Se imprime por pantalla el numero.
        print(numero)

#----------------------------------------------------------------------------

# Ejercicio 7: 
# Crea un programa que calcule la suma de todos los números comprendidos 
# entre 0 y un número entero positivo indicado por el usuario.
print(' 7 - Suma de todos los numeros entre 0 y un numero a ingresar.')
# Se pide al usuario que ingre por teclado un numero.
numero_indicado = int(input('Ingrese un numero: '))
sumatoria_7 = 0
# Estructura repetitiva cuya variable de iteracion toma valores desde el 0 
# hasta un numero indicado con paso 1
for i in range(0, numero_indicado+1, 1):
    # Acumulador al cual se le suma la variable de iteracion vuelta a vuelta. 
    sumatoria_7 += i
# Se imprime por pantalla la sumatoria comprtendida entre el 0 
# y el numero ingresado.
print(f'La sumatoria de los numeros entre 0 y {numero_indicado} es: {sumatoria_7}')

#----------------------------------------------------------------------------

# Ejercicio 8:
# Escribe un programa que permita al usuario ingresar 100 números enteros.
# indicar cuantos son pares, impares, negativos y positivos. 
print(' 8 - Determinar cuantos positivos, negativos, pares e impares hay en 100 numeros enteros a ingresar.')
contador_positivos = 0
contador_negativos = 0
contador_pares = 0
contador_impares = 0
# Estructura repetitiva cuya variable de iteracion toma 100 valores de 0 a 99.
for i in range(100):
    # Se pide al usuario que ingrese por teclado un numero entero.
    numero = int(input('Ingrese un numero: '))
    # Estructura condicional que verifica si el numero es positivo.
    if numero >= 0:
        # Se aumenta en 1 el contador de positivos. 
        contador_positivos += 1
    else:
        # Se aumenta en 1 el contador de negativos.
        contador_negativos += 1
    # Estructura condicional que verifica si el numero es par o no. 
    if numero % 2 == 0:
        # Se aumenta en 1 el contador de pares. 
        contador_pares += 1
    else:
        # Se aumenta en 1 el contador de impares.
        contador_impares += 1
# Se imprime por pantalla la cantidad de numeros pares, impares, 
# positivos y negativos obtenidos. 
print(f'Cantidad de numeros positivos: {contador_positivos}')
print(f'Cantidad de numeros negativos: {contador_negativos}')
print(f'Cantidad de numeros pares: {contador_pares}')
print(f'Cantidad de numeros impares: {contador_impares}')

#----------------------------------------------------------------------------

# Ejercicio 9: 
# Elabora un programa que permita al usuario ingresar 100 números enteros 
# y luego calcule la media de esos valores. (Nota: puedes probar el 
# programa con una cantidad menor, pero debe poder procesar 100 números 
# cambiando solo un valor).
print(' 9 - calcular el valor de la mediad de 100 numeros a ingresar. ')
# Se crea un conjunto sin elementos
numeros = []
# Estructura repetitiva cuya variable de iteracion toma 100 valores 
# entre (0 y 99). 
for i in range(100):
    # Se pide al usuario que ingrese por teclado un numero entero. 
    numero = int(input('Ingrese un numero: '))
    # Se agrega a la lista el numero ingresado como un elemento nuevo de la lista. 
    numeros.append(numero)
# Se calcula la media de los numeros utilizando "mean", esta funcion del 
# modulo statics calcula la media de los valeres que contiene una 
# lista/array/conjunto.
media = statistics.mean(numeros)
# Se imprime por pantalla  el valor calculado de la media. 
print(f'La media es: {media}')

#----------------------------------------------------------------------------

# Ejercicio 10:
# Escribe un programa que invierta el orden de los dígitos de un número 
# ingresado por el usuario. Ejemplo: si el usuario ingresa 547, 
# el programa debe mostrar 745.
print(' 10 - Invertir el orden de los digitos de un numero ingresado. ')
# Se pide al usuario que ingrese por teclado un numero entero. 
numero = int(input('Ingrese un numero: '))
# Se crea una cadena que contiene el numero ingresado en forma de string. 
cadena = str(numero)
numero_invertido = ''
caracter = ''
# Estructura repetitiva cuya variable de iteracion toma los valores 
# de las posiciones de los caracteres de la cadena que contiene el nombre 
# desde la ultima hasta la primera
for i in range(len(cadena), 0, -1):
    # Se accede por medio de la variable de iteracion a determinada posicion
    # de la cadena que contiene el numero ingresado. 
    caracter = cadena[i-1]
    # Se agrega desde el ultimo caracter hasta el primero en una cadena vacia
    numero_invertido = numero_invertido + str(caracter)
# Se imprime por pantalla el numero ingresado y el mismo con sus digitos 
# en orden inverso. 
print(f'El numero {numero}, con sus digitos en orden invertido es {numero_invertido}.')

#----------------------------------------------------------------------------



