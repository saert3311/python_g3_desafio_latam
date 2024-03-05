from sys import argv

CLP_A_ = {
    'SOL': 0,
    'ARS':  0,
    'USD': 0,
}

clp = 0
#Validar que se ingresaron los 4 valores

#Validar que todos los valores sean numeros enteros, decimales y positivos
#Usamos compresion de diccionarios para formatear y validar que los valores son numeros enteros, decimales y positivos

valores_validos = [float(valor) for valor in argv[1:] if valor.replace('.', '').isdigit()]

if len(valores_validos) != 4:
    print("Error: Los valores ingresados no son correctos")
    exit()

#Asignamos los valores a las variables del diccionario 

CLP_A_['SOL'] = valores_validos[0]
CLP_A_['ARS'] = valores_validos[1]
CLP_A_['USD'] = valores_validos[2]
clp = valores_validos[3]



print(f'Los {clp} pesos equivalen a:\n')
print(f'{round(CLP_A_["SOL"] * clp, 2)} Soles\n')
print(f'{round(CLP_A_["ARS"] * clp, 2)} Pesos Argentino\n')
print(f'{round(CLP_A_["USD"] * clp, 2)} Dolares Americanos\n')

