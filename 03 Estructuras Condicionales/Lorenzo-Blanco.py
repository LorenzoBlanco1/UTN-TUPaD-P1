from statistics import mode, median, mean
import random
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# Se muestra un saludo por pantalla
print('Hola!')
# Se impime por pantalla el eneunciado.
print('Ejercicio 1: \nSolicitar edad y determinar si es mayor de edad o no.')
# Se solicita al usuario que ingrese su edad por teclado.
edad = int(input('Ingrese su edad: '))

# Estructura Condicional que evalua si es mayor o no.
if edad >= 18:
    # Se imprime por pantalla un mensaje indicando que es mayor de edad.
    print('Es mayor de edad.')
else:
    # Se imprime por pantalla un mensaje indicando que no es mayor de edad.
    print('No es mayor de edad')
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso 
# contrario deberá mostrar el mensaje “Desaprobado”.

# Se imprime por pantalla el enunciado.
print('Ejercicio 2: \nSolicitar nota y determinar si esta Aprobado o Desaprobado.')

# Se solicita que el usuario ingrese una nota.
nota = float(input('Ingrese una nota: '))

# Estructura condicional que evalua si la nota es >= a 6.
# Se imprime por pantalla un mensaje indicando si esta Aprobado o Desaprobado.
if nota >= 6:
    # Se imprime por pantalla un mensaje indicando que esta Aprobado.
    print('Aprobado.')
else:
    # Se imprime por pantalla un mensaje indicando que esta Desaprobado.
    print('Desaprobado.')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3)  Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un 
# número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para 
# evaluar si un número es par o impar.

# Se imprime por pantalla el enunciado. 
print('Ejercicio 3: \nDeterminar si un numero ingresado es par o impar.')

# Se pide al usuario que igrese por teclado un numero.
numero = int(input('Ingrese un numero: '))

# Estructura condicional que determina si el numero es par o impar.

if numero % 2 == 0:
    # Se imprime por pantalla un mensaje indicando que el numero es par.  
    print(f'El numero {numero} es par.')
else: 
    # Se imprime por pantalla un mensaje indicando que es impar.  
    print(f'El numero {numero} es impar.')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4 ) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# Se imprime por pantala el enunciado.
print('Ejercicio 4: \nDeterminar categoria etaria.')

# Se solicita que el usuario ingrese su edad.
edad_ejercicio_4 = int(input('Ingrese su edad: '))

# Estructura condicional que determina a que categoria pertenece el usuario.
if edad_ejercicio_4 < 12:
    # Se imprime por pantalla un mensaje indicando que es un niño.
    print(f'De acuerdo a la edad {edad_ejercicio_4} se corresponde a la categoria "Niño".')
elif 12 <= edad_ejercicio_4 < 18:
    # Se imprime por pantalla un mensaje indicando que es un Adlecente.
    print(f'De acuerdo a la edad {edad_ejercicio_4} se corresponde a la categoria "Adolecente".')
elif 18 <= edad_ejercicio_4 < 30:
    # Se imprime por pantalla un mensaje indicando que es un Adulto/a joven.
    print(f'De acuerdo a la edad {edad_ejercicio_4} se corresponde a la categoria "Adulto/a joven".')
elif 30 <= edad_ejercicio_4:
    # Se imprime por pantalla un mensaje indicando que es un Adulto/a.
    print(f'De acuerdo a la edad {edad_ejercicio_4} se corresponde a la categoria "Adulto/a".')
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud 
# adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una 
# contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.

# Se imprime por pantalla el enunciado.
print('Ejercicio 5: \nDeterminar si una contraseña es valida.')
print('La contraseña es valda si tiene entre 8 y 14 caracteres.')
# Se solicita al usuario que ingrese por teclado una contraseña.
contraseña = input('Ingrese una contraseña: ')

# Se calcula con la funcion len cuantos caracteres tiene la cadena "contraseña".
longitud_contraseña = len(contraseña)

# Estructura condicional que evalua si la contraseña tiene entre 8 y 14 caracteres.
if 8 <= longitud_contraseña <= 14:
    # Se imprime por pantalla un mensaje indicando que la contraseña es correcta.
    print('Ha ingresado una contraseña correcta.') 
else:
    # Se imprime por pantalla un mensaje indicando que la contraseña ingresada no es correcta.
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres.')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números 
# escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, 
# negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Se imprime por pantalla el enunciado.
print('Ejercicio 6: \nDeterminar que tipo de Sesgo tiene una lista de numeros aleatorios: ')
print('Sesgo positivo: La media es mayor a la mediana y la mediana es mayor a la moda.')
print('Sesgo negativo: La media es menor a la mediana y la mediana es menor a la moda')
print('Sin Sesgo: La media es igual que la mediana e igual que la moda. ')

# Se define una lista de numeros aleatorios entre 1 y 100 de 50 elementos
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)
# Se calcula la moda de la lista de numeros aleatorios.
moda = mode(numeros_aleatorios)

# Se calcula la mediana de la lista de numeros aleatorios.
mediana = median(numeros_aleatorios)

# Se calcua la media de la lista de numeros aleatorios.
media = mean(numeros_aleatorios)
# Se imprme por pantalla la moda, mediana y media.
print(f'Moda: {moda}\nMediana: {mediana}\nMedia: {media}')
# Estructura condicional para determinar como se categoriza la lista en base al sesgo positivo, negativo o sin sesgo.
if (media > mediana) and (mediana > moda):
    # Se imprime por pantalla un mensaje indicando que existe Sesgo Positivo (media > mediana > moda)
    print('Hay Sesgo Positivo.')
elif (media < mediana) and (mediana < moda):
    # Se imprime por pantalla un mensaje indicando que existe Sesgo Negativo (media > mediana < moda)
    print('Hay Sesgo Negativo.')
else:
    # Se imprime por pantalla un mensaje indicando que se trata de una lista Sin Sesgo (media = mediana = moda)
    print('Sin Sesgo.')
       
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e 
# imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Se imprime por pantalla el enunciado.
print('Ejercicio 7: \nSolicitar una cadena al usuario:')
print('Si la cadena finaliza con vocal se imprime con un signo de exclamacion a final, sino tal cual se ingreso.')

# Se solicita al usuario que ingrese una cadena de caracteres.
cadena = input('Ingrese una cadena de caracteres: ')

# Estructura condicional que determina si la cadena termina con vocal o no.
if cadena[-1] in ('a', 'e', 'i', 'o', 'u'):
    # Se agrega un signo de exclamacion al final de la cadena.
    cadena = cadena + '!'
    # Se imprime por pantalla la cadena ingresada con un signo de excalmacion al final.
    print(f'La cadena ingresada con un signo de exclamacion al final es: \n{cadena}')
else:
    # Se muestra la cadena tal cual se ingreso.
    print(cadena)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# ● Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# ● Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# ● Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso 
# de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Se imprime por pantalla el enunciado.
print('Ejercicio 8: \nSolicitar nombre al usuario y numero de opcion:')

# Se solicta al usuario que ingrese su nombre.
nombre = input('Ingrese su nombre: ')

# Se mprime por pantalla el menu de opciones.
print('Opcion 1: Nombre en Mayusculas. EJ: LORENZO\nOpcion 2: Nombre en minusculas. EJ: lorenzo\nOpcion 3: Nombre con la primera letra en Mayuscula. EJ: Lorenzo')

# Se solcita al usuaro que ingrese una opcion: 
opcion = int(input('Ingrese una opcion: '))

# Estructura condicional que determina en base a la opcion elegida como se imprime por pantalla el nombre.
if opcion == 1:
    # Se convierten todos los caracteres alfabeticos en mayusculas.
    nombre = nombre.upper()
    # Se imprime por pantalla el nombre en mayusculas. 
    print(f'El nombre en mayusculas es: {nombre}')
elif opcion == 2:
    # Se convierten todos los caracteres alfabeticos en minusculas.
    nombre = nombre.lower()
    # Se imprime por pantalla el nombre en minusculas.
    print(f'El nombre en minusculas es: {nombre}')
elif opcion == 3:
    # Se convierte el primer caracter en mayuscula.
    nombre = nombre.title()   
    # Se imprime por pantalla el nombre con la primera letra en mayuscula. 
    print(f'El nombre con la primera letra en mayuscula es: {nombre}')
else:
    print('La opcion ingesada no es correcta. ')
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter
# e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# Se imprime por pantalla el enunciado.
print('Ejercicio 9: \nSolicitar al usuario la magntud de un terremoto, clasificar la magnitud del mismo segun la escala de Richter e impimir por pantalla.')

# Se solicita al usuario que ingrese por teclado la magnitud del terremoto.
magnitud_terremoto = float(input('Ingrese la magnitud del terremoto: '))

# Estructura condiconal que determina segun la escala de Richter la categoria.
if magnitud_terremoto < 3:
    # Se imprime por pantalla la categoria.
    print(f'Un terremoto de magnitud {magnitud_terremoto} es conciderado "Muy Leve".')
elif 3 <= magnitud_terremoto and magnitud_terremoto < 4:
    # Se imprime por pantalla la categoria.
    print(f'Un terremoto de magnitud {magnitud_terremoto} es conciderado "Leve".')
elif 4 <= magnitud_terremoto and magnitud_terremoto< 5:
    # Se imprime por pantalla la categoria.
    print(f'Un terremoto de magnitud {magnitud_terremoto} es conciderado "Moderado".')
elif 5 <= magnitud_terremoto and magnitud_terremoto < 6:
    # Se imprime por pantalla la categoria.
    print(f'Un terremoto de magnitud {magnitud_terremoto} es conciderado "Fuerte".')
elif 6 <= magnitud_terremoto and magnitud_terremoto< 7:
    # Se imprime por pantalla la categoria.
    print(f'Un terremoto de magnitud {magnitud_terremoto} es conciderado "Muy Fuerte".')
elif magnitud_terremoto >= 7:
    # Se imprime por pantalla la categoria.
    print(f'Un terremoto de magnitud {magnitud_terremoto} es conciderado "Extremo".')
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa 
# información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# Se imprime por pantalla el enunciado.
print('Ejercicio 10: \nSolicitar al usuario que ingrese en que hemisferio se encuentra (N/S), mes y dia.')

# Se soicita a usuario que ingrese hemisferio en que se encuentra, mes y dia.
hemisferio = input('Ingrese el hemisferio en el que se encuentra: ')
mes = input('Ingrese el mes: ')
dia = int(input(f'Ingrese el dia del mes {mes}: '))

# Estructura condicional que determina en que estacion se encuentra el usuario (se verifica que el mes y el dia sean validos).
if mes in ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre') and 0 < dia <= 31:
    # Hemisferio Sur.
    if hemisferio == 'sur':
        # Verano
        if (mes == 'diciembre' and (dia >= 21)) or (mes == 'enero' or mes == 'febrero') or (mes == 'marzo' and (dia < 21)):
            # Se imprime por pantalla la estacion.
            print('Se encuentra en Verano.')
        # Otoño
        if (mes == 'marzo' and (dia >= 21)) or (mes == 'abril' or mes == 'mayo') or (mes == 'junio' and (dia < 21)):
            # Se imprime por pantalla la estacion.
            print('Se encuentra en Otoño.')
        # Invierno.
        if (mes == 'junio' and (dia >= 21)) or (mes == 'julio' or mes == 'agosto') or (mes == 'septiembre' and (dia < 21)):
            # Se imprime por pantalla la estacion.
            print('Se encuentra en Invierno.')
        # Primavera.
        if (mes == 'septiembre' and (dia >= 21)) or (mes == 'octubre' or mes == 'noviembre') or (mes == 'diciembre' and (dia < 21)):
            # Se imprime por pantalla la estacion.
            print('Se encuentra en Primavera.')
    #Hemisferio Norte:
    elif hemisferio == 'norte':
        # Invierno
        if (mes == 'diciembre' and (dia >= 21)) or (mes == 'enero' or mes == 'febrero') or (mes == 'marzo' and (dia <= 20)):
            # Se imprime por pantalla la estacion.
            print('Se encuentra en Invierno.')
        # Primavera.
        if (mes == 'marzo' and (dia >= 21)) or (mes == 'abril' or mes == 'mayo') or (mes == 'junio' and (dia < 21)):
            # Se imprime por pantalla la estacion.
            print('Se encuentra en Primavera.')
        # Verano.
        if (mes == 'junio' and (dia >= 21)) or (mes == 'julio' or mes == 'agosto') or (mes == 'septiembre' and (dia < 21)):
            # Se imprime por pantalla la estacion.
            print('Se encuentra en Verano.')
        # Otoño.
        if (mes == 'septiembre' and (dia >= 21)) or (mes == 'octubre' or mes == 'noviembre') or (mes == 'diciembre' and (dia < 21)):
            # Se imprime por pantalla la estacion.
            print('Se encuentra en Otoño.')
    else:
        print('El hemisferio ingresado no es valido.')
else:
    print('El mes, el dia o ambos son incorrectos.')
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

