from Personaje import Personaje
from enfrentamiento import Enfrentamiento
#Archivo Principal del juego

if __name__ == '__main__':
    print('¡Bienvenido a Gran Fantasía!')
    jugador = Personaje(input('Por favor indique nombre de su personaje:'))

    print(jugador.estado)

    orco = Personaje('Orco')

    encuentro = Enfrentamiento(jugador, orco)
    encuentro.jugar()
