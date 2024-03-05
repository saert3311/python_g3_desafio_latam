'''
Se solicita devolver un informe resumido que exponga los meses que superan un cierto
umbral. El programa mayor_a.py debe retornar un diccionario con el mes y el valor asociado
siempre y cuando superen el umbral especificado. 
'''

ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}

import sys

#Validamos que se ingrese un valor

if len(sys.argv) != 2:
    print("Error: Debe ingresar un valor")
    sys.exit()

umbral = int(sys.argv[1])

if umbral < 0:
    print("Error: El umbral debe ser un número positivo")
    sys.exit()

#Usamos comprension de diccionarios para obtener el diccionario con los meses que superan el umbral

meses_mayor_a = {mes: valor for mes, valor in ventas.items() if valor > umbral}

#Imprimimos el diccionario obtenido

print("Meses que superan el umbral:")
print(meses_mayor_a)

