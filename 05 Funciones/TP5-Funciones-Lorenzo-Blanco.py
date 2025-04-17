import math
# Trabajo Funciones:

# Funciones:

def validar_entero(mensaje, minimo = float('-Inf'), maximo = float('Inf')):
    # Se pide al usuario que ingrese un numero por teclado.
    numero = int(input(mensaje))
    # Estructura repetitiva de permanencia que verifica que el numero este en un cierto rango.
    while (numero < minimo) or (numero > maximo):
        # Se imprime por pantalla un mensaje de error y se pide al usuario nuevamente que ingrese un numero.
        print('Error!')
        numero = int(input(mensaje))
    return numero

def validar_decimal(mensaje, minimo = float('-Inf'), maximo = float('Inf')):
    # Se pide al usuario que ingrese un numero por teclado.
    numero = float(input(mensaje))
    # Estructura repetitiva de permanencia que verifica que el numero este en un cierto rango.
    while (numero < minimo) or (numero > maximo):
        # Se imprime por pantalla un mensaje de error y se pide al usuario nuevamente que ingrese un numero.       
        print('Error!')
        numero = float(input(mensaje))
    return numero

def imprimir_mensaje(mensaje):
    # Esta funcion toma como argunmento un mensaje y lo imprime por pantalla.
    print(mensaje)
    
def saludar_usuario(nombre):
    # Esta funcion imprime por pantalla un saludo con un nombre recibido como argumento.
    imprimir_mensaje(f'Hola {nombre}!')

def informacion_personal(nombre, apellido, edad, residencia):
    # Esta funcion imprime por pantalla un mensaje con una estructura especifica utilizando los argumentos.
    imprimir_mensaje(f'Soy [{nombre}] [{apellido}], tengo [{edad}] años y vivo en [{residencia}]')
    
def calcular_area_circulo(radio):
    # Se almacena el calculo del area con el argumento (radio ingresado por usuario).
    area = math.pi * radio * radio
    return area

def calcular_perimetro_circulo(radio):
    # Se almacena el calculo del perimetro con el argumento (radio ingresado por el usuario).
    perimetro = 2 * math.pi * radio
    return perimetro

def segundos_a_horas(segundos):
    # Se divide la cantidad de segundos (argumento de la funcion) por 3600 para obtener su equivalente en horas.
    return segundos / 3600

def tabla_multiplicar(numero):
    # Se imprime por pantalla un mensae que indica que tabla de multiplicacion se va a mostrar.
    imprimir_mensaje(f'Tabla de Multiplicacion del numero {numero}')
    # Estructura de repeticion fija que va de 1 a 10.
    for i in range(1, 11):
        # Se imprime por pantalla la multiplicacion y el resultado de cada iteracion.
        imprimir_mensaje(f'{i} * {numero} = {i * numero}')

def operaciones_basicas(numero1, numero2):
    # Se crea un tupla cuyos elementos son las operaciones basicas entre los argumentos (numeros ingresados por el usuario).
    tupla = [(numero1 + numero2), (numero1 - numero2), (numero1 * numero2), (numero1 / numero2)]
    return tupla

def calcular_imc(peso, altura):
    # Se almacena el calculo del IMC calculado con los argumentos ingresados por el usuario (peso y altura).
    imc = peso / (altura * altura)
    return imc

def celsius_a_fahrenheit(celsius):
    # Se retorna el calculo de la equivalencia entre grados celsius y fahrenheit.
    return((celsius * (9/5)) + 32)

def calcular_promedio(numero1, numero2, numero3):
    # Se almacena el calculo del promedio de los argumentos (3 numeros ingresados por el usuario). 
    promedio = (numero1 + numero2 + numero3) / 3
    return promedio

# Programa principal.

#-------------------------------------------------------------------------------------------------------
# 1 - Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. 

# Esta funcion toma como argumento un mensaje y lo imprime por pantalla.
imprimir_mensaje('Hola Mundo!')

#-------------------------------------------------------------------------------------------------------

# 2 - Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y 
# devuelva un saludo personalizado. 

# Esta funcion toma como argumento el nombre del usuario e imprime por pantalla un saludo.
nombre = input('Ingrese su nombre: ')
saludar_usuario(nombre)

#-------------------------------------------------------------------------------------------------------

# 3 - Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) 
# y que imprima “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 

# Se pide al usuario que ingrese por teclado apellido, edad y residencia.
apellido = input('Ingrese su apellido: ')
edad = validar_entero('Ingrese su edad: ', 0)
residencia = input('Ingrese su lugar de residencia: ')

# Se imprime por pantalla una cadena con la informacion personale del usuario. 
informacion_personal(nombre, apellido, edad, residencia)

#-------------------------------------------------------------------------------------------------------

# 4 -  Crear dos funciones: 
# calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del 
# círculo. 

# Se pide al usuario que ingrese por teclado el radio.
radio = validar_entero('Ingrese el radio de un circulo: ', 0)

# Se imprime por pantalla el area y el perimetro calculados con el radio ingresado.
imprimir_mensaje(f'El area de un circulo cuyo radio es {radio} es: {calcular_area_circulo(radio)}')
imprimir_mensaje(f'El perimetro de un circulo cuyo radio es {radio} es: {calcular_perimetro_circulo(radio)}')

#-------------------------------------------------------------------------------------------------------

# 5 - Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como 
# parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y 
# mostrar el resultado usando esta función.

# Se pide al usuario que ingrese por teclado la cantidad de segundos.
segundos = validar_entero('Ingrese la cantidad de segundos: ', 0)

# Se imprime por pantalla el equivalente en horas de los segundos ingresados.
imprimir_mensaje(f'{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas.')

#-------------------------------------------------------------------------------------------------------

# 6 - Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y 
# imprima la tabla de multiplicar de ese número del 1 al 10. 

# Se pide al usuario que ingrese por teclado el numero que desea saber la tabla de multiplicacion
numero = validar_entero('Ingrese el numero que desea saber su tabla de multiplicaion: ', 0)

# Se imprime por pantalla la tabla de multiplicacion del numero ingresado.
tabla_multiplicar(numero)

#-------------------------------------------------------------------------------------------------------

# 7 - Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y 
# devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

# Se pide al usuario que ingrede por teclado los numero a realizar las operaciones basicas.
numero1 = validar_entero('Igrese el primer numero: ', 0)
numero2 = validar_entero('Ingrese el segundo numero: ', 0)

# Se crea una tupla conn los esultados de dichas operaciones basicas.
tupla = operaciones_basicas(numero1, numero2)

# Se imprime por pantalla las operaciones con sus respectivos resultados.
imprimir_mensaje(f'{numero1} + {numero2} = {tupla[0]}')
imprimir_mensaje(f'{numero1} - {numero2} = {tupla[1]}')
imprimir_mensaje(f'{numero1} * {numero2} = {tupla[2]}')
imprimir_mensaje(f'{numero1} / {numero2} = {tupla[3]}')

#-------------------------------------------------------------------------------------------------------

# 8 - Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura 
# en metros, y devuelva el índice de masa corporal (IMC). 

# Se pide al usuario que ingrese por teclado su peso y altura.
peso = validar_decimal('Ingresar su peso en kg: ', 0)
altura = validar_decimal('Ingrese su altura en metros: ', 0)

# Se imprime por pantalla el IMC calculado.
imprimir_mensaje(f'De acurdo al peso {peso} KG y la altura {altura} metros, el IMC es: {calcular_imc(peso, altura)}')

#-------------------------------------------------------------------------------------------------------

# 9 - Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados 
# Celsius y devuelva su equivalente en Fahrenheit. 

# Se pide al usuario que ingrese por tecaldo una temperatura en grados celsius.
temperatura_celsius = validar_decimal('Ingrese una temperatura en grados celsius: ')

# Se imprime por pantalla el equivalente en grados fahrenheit de la temperatura en grados celsius.
imprimir_mensaje(f'{temperatura_celsius} Grados Celsius equivalen a {celsius_a_fahrenheit(temperatura_celsius)} Grados Fahrenheit.')

#-------------------------------------------------------------------------------------------------------

# 10 - Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y 
# devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# Se pide al usuario que ingrese por teclado 3 numeros.
numero1 = validar_decimal('Ingrese el primer numero: ', 0)
numero2 = validar_decimal('Ingrese le segundo numero: ', 0)
numero3 = validar_decimal('Ingrese el cuarto numero: ', 0)

# Se imprime por pantalla el promedio de los 3 numeros ingresados. 
imprimir_mensaje(f'El promedio de los numeros {numero1}, {numero2}, {numero3} es: {calcular_promedio(numero1, numero2, numero3)}')
