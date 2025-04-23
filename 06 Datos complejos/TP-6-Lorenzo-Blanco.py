# TRABAJO PRACTICO 6 - LISTAS

#-----------------------------------------------------------------------------------------------
# 1 - Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar
# la función range.
print('---------------------------------------------------------------------------------------')
# Se crea una lista con valores del 1 al 9 y se almacena en lista_range.
lista_range = list(range(0,101, 4))

# Se imprime por pantalla la lista creada. 
print(' 1 - Lista con los numeros del 1 al 100 multiplos de 4:')
print(f'Lista = {lista_range}')

#-----------------------------------------------------------------------------------------------

# 2 - Crear una lista con 5 elementos y mostrar el penultimo.
print('---------------------------------------------------------------------------------------')
# Se crea una lista con 5 elementos (cualquierasean).
lista2 = ['Lorenzo', 'Blanco', 21, 'Administrativo', 'Cordoba']

# Se imprime por pantalla el penultimo elemento de la lista accediendo con subindice 
# negativo y la lista
print(' 2 - Lista y penultimo elemento: ')
print(f'Lista: {lista2}')
print(f'El penultimo elemento de la lista es: {lista2[-2]}')

#-----------------------------------------------------------------------------------------------

# 3 - Crear una lista vacia, agregar 3 palabras con append e imprimir.
print('---------------------------------------------------------------------------------------')
# Se crea una lista vacia y se almacena en lista3.
lista3 = []

# Se agregan 3 palabras a la lista (cada una como un elemento.)
lista3.append('Lorenzo')
lista3.append('Blanco')
lista3.append('Programacion')

# Se imprime por pantalla la lista resultante.
print(f' 3 - Lista = {lista3}')

#-----------------------------------------------------------------------------------------------

# 4 - Reemplazar el segundo y el ultimo valor de la lista animales con las palabras 
# "loro" y "oso" respectivamente.
print('---------------------------------------------------------------------------------------')
# Se crea y se imprime por pantalla la lista original.
animales = ['perro', 'gato', 'conejo', 'pez']
print(f' 4 - Lista de animales: {animales}')

# Se modifican el segundo y ultimo elemento utilizando subindices. 
animales[1] = 'loro'
animales[-1] = 'oso'

# Se imprime por pantalla la lista modificada.
print(f'Lista de animales modificada: {animales}')

#-----------------------------------------------------------------------------------------------

# 5 - Analizar el sigueinte programa y explicar con tus palabras que es lo que realiza
print('---------------------------------------------------------------------------------------')
numeros= [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(f' 5 - Lista numeros {numeros}')

# Se crea una lista con numeros [8, 15, 3, 22, 7] y se elimina el mayor utilizando
# remove y max, max recibe como argumento la lista y remove el elemento.

#-----------------------------------------------------------------------------------------------

# 6 - Crear una lista con numeros del 10 al 30 (incluido), haciendo saltos de 5 en 5
# y mostrar por pantalla a los 2 primeros. 
print('---------------------------------------------------------------------------------------')

# Se crea una lista utilizando la funcion range y se almacena en lista6. 
lista6 = list(range(10, 31, 5))

# Se imprime por pantalla los primeros 2 elementos de la lista utilizando slicing.
print(f' 6 - Lista con numeros del 10 al 30 con saltos de 5 en 5: {lista6}')
print(f'Los primeros 2 elementos de la lista son {lista6[0:2]}')

#-----------------------------------------------------------------------------------------------

# 7 -  Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por
#dos nuevos valores cualesquiera. 
print('--------------------------------------------------------------------------------------')
# Se crea una lista de autos y almacena en autos. 
autos = ['sedan', 'polo', 'suran', 'gol']

# Se imprime por pantalla la lista original. 
print(f' 7 - Lista original: {autos}')

# Se reemplazan los valores de los indices 1 y 2 (elementos centrales).
autos[1] = 'Supra'
autos[2] = 'RX-7'

# Se imprime por pantalla la lista original y la lista con los elementos reemplazados. 
print(f'Lista modificada: {autos}')

#-----------------------------------------------------------------------------------------------

# 8 -  Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando 
# append directamente. Imprimir la lista resultante por pantalla. 
print('---------------------------------------------------------------------------------------')
# Se crea una lista vacia llamada dobles.
dobles = []

# Se agregan 3 elementos utilizanod append, el doble de 5, 10 y 15 respectivamente.
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

# Se imprime por pantalla la lista.
print(f' 8 - Lista con el doble de 5, 10, 15: {dobles}')

#-----------------------------------------------------------------------------------------------

# 9 - Dada la lista "Compras", cuyos elementos representan los productos comprados por
# diferentes clientes. 
compras = [['pan', 'leche'], ['arroz', 'fideos', 'salsa'], ['agua']]
print('---------------------------------------------------------------------------------------')
# Se imprime por pantalla la lista original.
print(f' 9 - Lista original: {compras}')

# Se agrega el elmento 'jugo' a la lista del tercer cliente. 
compras[2].append('jugo')

# Se reemplaa 'fideos' por 'tallarines' en la lista del segundo cliente. 
compras[1][1] = 'tallarines'

# Se elimina 'pan' de la lista del primer cliente.
compras[0].remove('pan')

# Se imprime por pantalla la lista modificada. 
print(f'Lista modificada: {compras}')

#-----------------------------------------------------------------------------------------------

# 10 - Elaborar una lista anidada llamada 'lista_anidada' que contenga los elementos: 
#● Posición lista_anidada[0]: 15 
#● Posición lista_anidada[1]: True 
#● Posición lista_anidada[2][0]: 25.5 
#● Posición lista_anidada[2][1]: 57.9 
#● Posición lista_anidada[2][2]: 30.6 
#● Posición lista_anidada[3]: False 
print('---------------------------------------------------------------------------------------')

lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]]

# Se imprime por pantalla la lista creada.
print(f' 10 - Lista anidada: {lista_anidada} ')

print('---------------------------------------------------------------------------------------')

#-----------------------------------------------------------------------------------------------
print('FIN DEL PROGRAMA')