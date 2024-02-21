'''
Se pide crear el programa cachipun.py, donde el usuario entregará como
argumento: piedra, papel o tijera. Para que el computador pueda jugar escogerá un
valor al azar. Para eso se solicita investigar random.choice() de la librería random.

'''

import sys
import random

if len(sys.argv) != 2:
    print("Error: Debe ingresar un valor")
    sys.exit()

jugador = sys.argv[1]

if jugador != 'piedra' and jugador != 'papel' and jugador != 'tijera':
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
    sys.exit()

computador = random.choice(['piedra', 'papel', 'tijera'])
print(f"Tú jugaste {jugador}")
print(f"El computador jugo {computador}")

if jugador == computador:
    print("Empate 😑")
elif jugador == 'piedra' and computador == 'tijera':
    print("Ganaste!! 😁")
elif jugador == 'papel' and computador == 'piedra':
    print("Ganaste!! 😁")
elif jugador == 'tijera' and computador == 'papel':
    print("Ganaste!! 😁")
else:
    print("Perdiste 😒")

