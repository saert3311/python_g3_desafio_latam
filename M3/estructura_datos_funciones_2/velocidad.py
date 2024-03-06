'''
● Para ello se pide determinar una funcionalidad que calcule el promedio de una lista de
velocidades. El servidor donde se pretende instalar esta funcionalidad no cuenta con
mucha capacidad por lo que se pide no depender de librerías externas.
Listar las posiciones de todas las correas transportadoras que están sobre el
promedio
'''

velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

def promedio_velocidades(velocidades):
    '''
    Calcula el promedio de una lista de velocidades
    '''
    return sum(velocidades) / len(velocidades)

def posiciones_sobre_promedio(velocidades, promedio):
    '''
    Devuelve las posiciones de las velocidades que estan sobre el promedio
    '''
    return [i for i, velocidad in enumerate(velocidades) if velocidad > promedio]

promedio = promedio_velocidades(velocidad)

sobre_promedio = posiciones_sobre_promedio(velocidad, promedio)

print(sobre_promedio)