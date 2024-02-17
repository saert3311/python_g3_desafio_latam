print('Programa para calcular velocidad de escape\n')

radio = input('Ingrese el radio en Kms:\n')

gravedad = input('Ingrese la gravedad en m/s:\n')

##Validar que los datos sean numericos y calcular la velocidad de escape

if radio.isnumeric() and gravedad.replace(".", "").isnumeric():
    radio = float(radio)
    gravedad = float(gravedad)
    velocidad = (2 * gravedad * radio * 1000) ** 0.5
    print(f'La velocidad de escape es de {round(velocidad, 2)} m/s')
else:    
    print('Datos no validos')