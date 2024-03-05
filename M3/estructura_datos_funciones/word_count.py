'''
Genere un archivo llamado word_count.py que importe un texto a Python y realice las
siguientes tareas:
● Utilizando una estructura de datos apropiada, cuente la cantidad de caracteres
distintos que componen un texto.
● Cuente el número de palabras distintas que componen el texto ingresado. Para
separar un texto por espacios puede utilizar el método .split("").

'''

from sys import argv

#validar que se ingreso un archivo
if len(argv) != 2:
    print("Error: Debe ingresar un archivo")
    exit()

nombre_archivo = argv[1]

with open(nombre_archivo, 'r') as archivo:
    texto = archivo.read()

#Contar la cantidad de caracteres distintos que componen un texto

caracteres = set(texto)

palabras = texto.split(" ")
palabras_distintas = set(palabras)
print(f"La cantidad de caracteres distintos es: {len(caracteres)}")
print(f"La cantidad de palabras distintas es: {len(palabras_distintas)}")