from usuario import Usuario
import json
from datetime import datetime
import os

'''
Leer línea a línea el archivo usuarios.txt, y crear
una instancia de Usuario a partir de los datos de cada línea leída. estas lineas estan en formato json

En el mismo archivo, manejar las posibles excepciones al leer cada línea y/o generar
cada instancia, y agregar la excepción en un archivo error.log, debe contener la hora y fecha de la excepción

'''

def leer_usuarios():
    with open(os.path.join(os.path.dirname(__file__), 'usuarios.txt'), 'r') as archivo: #podriamos capturar tambien errores al abrir el archivo
        for linea in archivo:
            try:
                datos = json.loads(linea)
                usuario = Usuario(datos['nombre'], datos['apellido'], datos['email'], datos['genero'])
                print(usuario)
            except Exception as e:
                with open('error.log', 'a') as log:
                    log.write(f'{datetime.now()} - {e}\n')
                continue

if __name__ == '__main__':
    leer_usuarios()
