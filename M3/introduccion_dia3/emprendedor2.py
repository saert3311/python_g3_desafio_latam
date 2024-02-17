'''
 Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados,
los usuarios normales y los usuarios premium a los cuales se les cobrará una
suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que
permita considerar el caso recién expuesto. Para ello modifica la fórmula de utilidades
en la cual se solicite mediante input() los parámetros de entrada precios de
suscripción P, así como el número de usuarios Unormal y Upremium y el gasto total GT.
'''

print('Programa para calcular utilidades V2\n')

precio = input('Ingrese el precio de suscripcion:\n')

usuarios_normales = input('Ingrese el numero de usuarios normales:\n')

usuarios_premium = input('Ingrese el numero de usuarios premium:\n')

gastos_totales = input('Ingrese el gasto total:\n')

##Validar que los datos sean numericos y calcular las utilidades

if precio.isnumeric() and usuarios_normales.isnumeric() and usuarios_premium.isnumeric() and gastos_totales.isnumeric():
    precio = float(precio)
    usuarios_normales = float(usuarios_normales)
    usuarios_premium = float(usuarios_premium)
    gastos_totales = float(gastos_totales)
    utilidades = (precio * (usuarios_normales + usuarios_premium * 1.5)) - gastos_totales
    print(f'Las utilidades son de {round(utilidades, 2)}')
else:
    print('Datos no validos')
    