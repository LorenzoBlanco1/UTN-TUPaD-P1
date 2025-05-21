# TRABAJO PRACTICO RECURSIVIDAD. 

def validar_natural(mensaje):
    numero = int(input(mensaje))
    while numero < 0:
        print('Error, El número debe ser positivo y entero, intente nuevamente!')
        numero = int(input(mensaje))
    return numero

def factorial(numero): 
    return 1 if numero == 1 or numero == 0 else numero * factorial(numero - 1)

def fibonacci(numero):
    if numero == 1: 
        return 1
    elif numero == 0: 
        return 0
    else: 
        return numero + fibonacci(numero - 1)
    
def potencia(base, exponente): 
    if exponente == 0:
        return 1
    else: 
        resultado = base * potencia(base, exponente-1)
        return resultado

def decimal_a_binario(numero_decimal): 
    if numero_decimal == 0: 
        return '0'
    else: 
        return decimal_a_binario(numero_decimal // 2) + str(numero_decimal % 2)
        
def es_palindromo(cadena): 
    if len(cadena) <= 1: 
        return True
    elif cadena[0] == cadena[-1]: 
        return es_palindromo(cadena[1:-1])
    else:
        return False
   
def suma_digitos(numero): 
    if numero < 10:
        return numero
    else: 
        return numero % 10 + suma_digitos(numero // 10)

def contar_bloques(numero): 
    if numero == 1: 
        return 1
    else: 
        return numero + contar_bloques(numero - 1)

def contar_digito(numero, digito):
    if numero < 10: 
            return 1 if numero == digito else 0
    else: 
        ultimo_digito = numero % 10
        resto_numero = numero // 10
        return 1 + contar_digito(resto_numero, digito) if ultimo_digito == digito else contar_digito(resto_numero, digito)
        
def validar_rango(numero, minimo, maximo): 
    while numero < minimo or numero > maximo:
        print(f'Error, debe ingresar un numero entre {minimo} y {maximo}!')
        numero = validar_natural(f'Ingrese un número entre {minimo} y {maximo}: ')
    return numero
        
#-------------------------------------------------------------------------------------------------------------

# 1 - Crear una funcion recursiva que calcule el factorial de un número. Luego utiliza la funcion para 
# calcular y mostrar el factoria de todos los enteros entre 1 y el Nª a ingresar por el usuario. 

cantidad_factoriales = validar_natural('Ingrese la cantidad de factoriales desde 1 que desea mostrar: ')
for i in range(0, cantidad_factoriales + 1):
    print(f'Factorial de {i}: {factorial(i)}')


#-------------------------------------------------------------------------------------------------------------

# 2 - Crea una funcion recursiva que calcule el valor de la serie de fibonacci en la poscion indicada. 
# Posteriormente muestre a serie completa hastaa posicion que el usuario especifique. 

numero_fibonacci = validar_natural('Ingrese la posicion de la serie de fibonacci que desea saber el valor: ')
print(f'El valor de la serie de fibonacci para el numero {numero_fibonacci} es: {fibonacci(numero_fibonacci)}')

numero_limite_serie_fibonacci = validar_natural('Ingresar Nº hasta el cual se desea mostrar el valor: ')
for i in range(0, numero_limite_serie_fibonacci + 1):
    print(f'Fibonacci Nº {i}: {fibonacci(i)}')


#-------------------------------------------------------------------------------------------------------------

# 3 - Crear una funcion recursiva que calcule la potencia de un numero base elevado a un exponente.
# hasta la posicion que el usuario especifique. 

base = validar_natural('Ingrese la base de la potencia a calcular: ')
exponente = validar_natural('Ingrese el exponente de la potencia a calcular: ')

potencia = potencia(base, exponente)

print(f'La potencia que resulta de elevar {base} a {exponente} es: {potencia}')

#-------------------------------------------------------------------------------------------------------------

# 4 - Crea una función que que reciba un número entero positivo en base decimal y entregue su 
# representación en binario como cadena de texto.

decimal = validar_natural('Ingrese el numero decimal que quiere convertir a binario: ')
print(f'El numero {decimal} en binario es: {decimal_a_binario(decimal)}')


#-------------------------------------------------------------------------------------------------------------

# 5 - Implementar función llamada es_palindromo que reciba una cadena de teto sin espacios ni tildes
# y devuelva verdadero si es palindromo y falso si no lo es. 

palabra = input('Ingrese una palabra / Cadena de texto: ')
if es_palindromo(palabra): 
    print(f'La cadena "{palabra}" es palindromo. ')
else: 
    print(f'La cadena "{palabra}" no es palindromo. ')
    

#-------------------------------------------------------------------------------------------------------------

# 6 - Escribir una funcion recursiva en pyton llamada suma_digitos(n) que reciba n numero entero positivo
# y devuelva la suma de todos sus digitos. 

numero = validar_natural('Ingrese un número entero positivo: ')
print(f'La suma de los digitos del numero {numero} es: {suma_digitos(numero)}')

#-------------------------------------------------------------------------------------------------------------

# 7 - Escribir una funcion recursiva contar_bloques(n) que reciba el numero de bloques de la base y 
# devuelva el total de bloques que se necesita para construir una piramide.

cantidad_bloques_base = validar_natural('Ingrese la cantidad de bloques de la base de la piramide: ')
print(f'La cantidad de bloques de la piramide cuya base tiene {cantidad_bloques_base} bloques es: {contar_bloques(cantidad_bloques_base)}')

#-------------------------------------------------------------------------------------------------------------

# 8 - Escribir una funcion recursiva llamada contar_digito(numero, digito) que reciba un Nº natural
# y un digito del 0 al 9, y devuleva cuantas veces aparece ese digito dentro del numero. 

numero = validar_natural('Ingrese un número entero positivo: ')
digito = (validar_rango(validar_natural('Ingrese un numero entero positivo entre 0 y 9: '), 0, 9))
print(f'La cantidad de veces que se encuentra el digito {digito} en el número {numero} es: {contar_digito(numero, digito)}')
