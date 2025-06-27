# TP Estructuras de Datos Complejos: 


# 1) Dado el diccionario precios_frutas.

precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:

precios_frutas['Naranja'] = 1200 ; precios_frutas['Manzana'] = 1700 ; precios_frutas['Pera'] = 2300
print('Diccionario de Datos: ')
print(precios_frutas)

#-------------------------------------------------------------------------------------------------------

# 2) Actualizar los precios de Banana = 1330, Manzana = 1700, Melon = 2800.

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print('Diccionario Actualizado...')

print(precios_frutas)

#-------------------------------------------------------------------------------------------------------

# 3) Crear una lista que contenga las frutas que no tienen precio en base a precios_frutas

lista_frutas = list(precios_frutas.keys())        
print(F'Lista de Frutas sin precio: {lista_frutas}')

#-------------------------------------------------------------------------------------------------------

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
agenda = {}
for i in range(5):
    nombre = input('Ingrese el nombre del contacto: ')
    numero = int(input(F'Ingrese el número de telefono de {nombre}: '))
    agenda[nombre] = numero
    
contacto = input('Ingrese el nombre del contacto al que desea llamar: ')
if contacto in agenda:
    print(F'El número es: {agenda[contacto]}')
else: 
    print('Ese contacto no está en la agenda. ')
    
    
#-------------------------------------------------------------------------------------------------------


# 5) Solicita al usuario una frase e imprime las palabras únicas y las veces que aparecen. 

frase = input('Ingrese una Frase: ')

palabras = frase.lower().split()
unicas = set(palabras)
conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else: 
        conteo[palabra] = 1
        
print(F'Las palabras son: {unicas}')
print(F'Diccionario con conteo de cada palabra: {conteo}')

#-------------------------------------------------------------------------------------------------------

# 6) Permití ingresar 3 nombres, para cada uno una tupla de 3 notas. Luego, mostrá el promedio de c/u.

alumnos = {}

for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingresá nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

# Mostrar promedios
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"promedio {alumno}: {promedio:.2f}")
    
    
#-------------------------------------------------------------------------------------------------------

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y 2:
# Mostrar los que aprobaron ambos parciales, solo uno de los dos, estudiantes aprobaron uno almenos. 

alumnos = {'Lorenzo': (7, 8, 9), 'Javier': (5, 6, 7), 'Joan': (10, 9, 10)}
promedios = {alumno: sum(notas)/len(notas) for alumno, notas in alumnos.items()}
print(F'Estudiantes aprobados: {promedios}')

#-------------------------------------------------------------------------------------------------------

# 8)  Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#    Se debe poder consultar stock, agragar unidades al stock existente y agragar prducto. 

stock = {'Azúcar': 10, 'Harina': 5}
producto = 'Azúcar'
if producto in stock:
    stock[producto] += 3

producto_nuevo = 'Café'
if producto_nuevo not in stock:
    stock[producto_nuevo] = 8
    
print(F'Stock de productos: {stock}')

#-------------------------------------------------------------------------------------------------------
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda_eventos = {('Lunes', '10:00'): 'Reunión', ('Martes', '14:00'): 'Clase'}

print(f'Agenda Eventos: {agenda_eventos}')

consulta_dia = input('Ingrese el día que desea saber si hay actividades: ')
consulta_hora = input('Ingrese la hora que desea saber si hay actividades: ')
consulta = (consulta_dia, consulta_hora)

if consulta in agenda_eventos:
    print(f'Actividad programada: {agenda_eventos[consulta]}')
else:
    print(f'No hay eventos programados para el día/hora {consulta}')

#-------------------------------------------------------------------------------------------------------

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario
#    donde las capitales sean claves y los paises valores. 


paises_capitales = {'Argentina': 'Buenos Aires', 'Francia': 'París', 'Japón': 'Tokio'}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print(F'Diccionario original: {paises_capitales}')
print(F'Diccionario invertido: : {capitales_paises}')

