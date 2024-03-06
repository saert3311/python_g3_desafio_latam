'''
Crear un script llamado ong.py que contenga las siguientes funciones:
○ Una función que calcule el factorial.
○ Una función que calcule la productoria.
○ Una función que permita controlar los cálculos. Esta función se debe invocar
de la siguiente manera:
calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)
'''

def factorial(n):
    '''
    Calcula el factorial de un numero
    '''
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def productoria(lista):
    '''
    Calcula la productoria de una lista
    '''
    productoria = 1
    for i in lista:
        productoria *= i
    return productoria

def calcular(**kwargs):
    '''
    Controla los calculos
    '''
    for key, value in kwargs.items():
        if key.startswith('fact'):
            print(f'El factorial de {value} es {factorial(value)}')
        elif key.startswith('prod'):
            print(f'La productoria de {value} es {productoria(value)}')



if __name__ == '__main__':
    calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)
