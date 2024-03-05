'''
Se requiere la construcción de una aplicación interactiva primeros_auxilios.py que
entregue los distintos pasos a seguir dependiendo de las respuestas que el usuario entrega
en tiempo real
'''
import sys

#Validamos que se ingrese un valor

#funcion para validar la respuesta es si o no y simplificamos las respuestas a booleanos

def validar_respuesta(respuesta):
    if respuesta != 'si' and respuesta != 'no':
        print("Respuesta inválida: Debe ser si o no.")
        sys.exit()
    
    if respuesta == 'si':
        return True
    else:
        return False


print('Inicio del programa')

#preguntamos si la persona esta consciente
respuesta = validar_respuesta(input('¿Responde a estimulos? (si/no): '))

if respuesta:
    print('Valorar la necesidad de llevarlo al hospital mas cercano')   
else:
    print('Abrir la via aerea')
    respuesta = validar_respuesta(input('¿Respira? (si/no): '))

    if respuesta:
        print('Permitirle posicion de suficiente ventilacion')

    else:
        print('Administrar 5 ventilaciones y llamar a Ambulancia')

        ambulancia = False #inicializamos en false

        while not ambulancia:
            respuesta = validar_respuesta(input('¿Signos de Vida? (si/no): '))

            if respuesta:
                print('Reevaluar a la espera de la ambulancia')
            else:
                print('Administrar Compresiones Toracicas hasta que llegue ambulancia')

            ambulancia = validar_respuesta(input('¿Llego la ambulancia? (si/no): '))


print('FIN')