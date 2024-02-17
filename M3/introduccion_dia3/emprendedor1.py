'''
Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente
para calcular las utilidades de un proyecto. Para ello utiliza input() para solicitar
como dato el precio de suscripción P, el número de usuarios U y el gasto total GT.
'''

print('Programa para calcular utilidades\n')

precio = input('Ingrese el precio de suscripcion:\n')

usuarios = input('Ingrese el numero de usuarios:\n')

gastos_totales = input('Ingrese el gasto total:\n')

##Validar que los datos sean numericos y calcular las utilidades

if precio.isnumeric() and usuarios.isnumeric() and gastos_totales.isnumeric():
    precio = float(precio)
    usuarios = float(usuarios)
    gastos_totales = float(gastos_totales)
    utilidades = (precio * usuarios) - gastos_totales
    print(f'Las utilidades son de {round(utilidades, 2)}')
else:
    print('Datos no validos')
