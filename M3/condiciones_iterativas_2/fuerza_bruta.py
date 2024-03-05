'''
El programa fuerza_bruta.py debe intentar todas las combinaciones de letras posibles, en
orden alfabético, hasta que la combinación de letras sea igual a la de la contraseña indicada.
Deberá hacer este proceso letra por letra, de izquierda a derecha.
Consideraciones
● Utilizar from string import ascii_lowercase
○ ascii_lowercase es un string con todas las letras del abecedario en
minúsculas (sin la ñ).
● No considerar la ñ.
● Considera mayúsculas y minúsculas como una misma letra.
● Se considera "intento" cada vez que se compara una letra.
'''

from string import ascii_lowercase
import getpass

#Validamos que se ingrese un valor

contrasena = getpass.getpass("Ingrese la contraseña: ")

#Convertimos la contraseña a minusculas

contrasena = contrasena.lower()

#Inicializamos la variable intentos en 0

intentos = 0

#Inicializamos la variable combinacion en un string vacio

combinacion = ''

#Iteramos sobre la longitud de la contraseña

for i in range(len(contrasena)):
    #Iteramos sobre el abecedario
    for letra in ascii_lowercase:
        intentos += 1
        #print(f"Intento: {intentos} Combinacion: {combinacion + letra}")
        if letra == contrasena[i]:
            combinacion += letra
            break
        #Si la combinacion es igual a la contraseña
if combinacion == contrasena:
    #Imprimimos el resultado
    print(f"La contraseña fue forzada en {intentos} intentos")
