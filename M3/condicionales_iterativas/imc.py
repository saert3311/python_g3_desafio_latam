import sys

if len(sys.argv) != 3:
    print("Error: Debe ingresar dos valores")
    sys.exit()

if not sys.argv[1].isdigit() and not sys.argv[2].isdigit():
    print("Error: Los valores ingresados no son números")
    sys.exit()

peso = float(sys.argv[1])
altura = float(sys.argv[2])

# Convertir altura a metros si está en centímetros
if altura <= 0 or altura > 2.5:
    altura_metros = altura / 100
else:
    altura_metros = altura

imc = peso / (altura_metros ** 2)

print(f"Tu IMC es de {round(imc, 2)}\n")

print("La clasificación OMS es:", end=' ')
if imc < 20:
    print("Peso bajo")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")


