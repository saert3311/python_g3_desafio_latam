'''
Considera ahora una tercera versión llamada emprendedor3.py utilizando la fórmula
original de utilidades donde el usuario ingrese el precio de suscripción P, el número de
usuarios normales U y los gastos GT. Adicionalmente, solicita las utilidades del año
anterior Uanterior, todo esto mediante input(). El programa debe calcular las utilidades
actuales y mostrar la razón entre las utilidades actuales y las del año anterior con dos
decimales.
'''

print('Programa para calcular utilidades V3\n')

precio = input('Ingrese el precio de suscripcion:\n')

usuarios = input('Ingrese el numero de usuarios:\n')

gastos_totales = input('Ingrese el gasto total:\n')

utilidades_anterior = input('Ingrese las utilidades del año anterior:\n')

##Validar que los datos sean numericos y calcular las utilidades

if precio.isnumeric() and usuarios.isnumeric() and gastos_totales.isnumeric() and utilidades_anterior.isnumeric():
    precio = float(precio)
    usuarios = float(usuarios)
    gastos_totales = float(gastos_totales)
    utilidades_anterior = float(utilidades_anterior)
    utilidades = (precio * usuarios) - gastos_totales
    print(f'Las utilidades son de {round(utilidades, 2)}')
    print(f'La razon entre las utilidades actuales y las del año anterior es de {round(utilidades/utilidades_anterior, 2)}')
else:
    print('Datos no validos')
    