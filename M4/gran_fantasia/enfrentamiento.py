#Logica de los enfrentamientos
#Se me ocurre que los enfrentamientos pueden cambiar parametros es mas sencillo hacerlo desde aqui
#Por eso el metodo de las probabilidades esta aqui
import random, time

class Enfrentamiento:
    def __init__(self, personaje1, personaje2):
        self.__personaje1 = personaje1
        self.__personaje2 = personaje2
        self.__seed = time.time()
        self.__probabilidades = 0 #iniciamos en 0
        self.__costo_victoria = 50
        self.__costo_derrota = -30
        print(f'Oh no a aparecido un {self.__personaje2.nombre}\n')

    def iniciar(self):
        if self.__personaje1 > self.__personaje2:
            print(f'{self.__personaje1.nombre} tienes 66% de probabilidades de ganar a {self.__personaje2.nombre}')
            self.__probabilidades = 66
        elif self.__personaje1 < self.__personaje2:
            print(f'{self.__personaje2.nombre} tienes 33% de probabilidades de ganar a {self.__personaje1.nombre}')
            self.__probabilidades = 33
        else:
            print(f'{self.__personaje1.nombre} tienes 50% de probabilidades de ganar a {self.__personaje2.nombre}')
            self.__probabilidades = 50
        print(f'Si ganas, ganarás {self.__costo_victoria} puntos de experiencia y {self.__personaje2.nombre} perderá {self.__costo_derrota}.\n')
        print(f'Si pierdes, perderas {self.__costo_derrota} puntos de experiencia y {self.__personaje2.nombre} ganara {self.__costo_victoria}.\n')
    
    def resultado_ataque(self):
        return True if random.randint(1, 100) <= self.__probabilidades else False

    def resultado_ronda(self):
        if self.resultado_ataque():
            print(f'{self.__personaje1.nombre} ha ganado')
            self.__personaje1.asumir_experiencia(self.__costo_victoria)
            self.__personaje2.asumir_experiencia(self.__costo_derrota)
        else:
            print(f'{self.__personaje2.nombre} ha ganado')
            self.__personaje1.asumir_experiencia(self.__costo_derrota)
            self.__personaje2.asumir_experiencia(self.__costo_victoria)
        print(self.__personaje1.estado, end='\n')
        print(self.__personaje2.estado, end='\n')

    def jugar(self):
        desicion = 1
        while desicion == 1:
            self.iniciar()
            desicion = int(input('¿Qué deseas hacer?\n1. Atacar\n2. Huir\n'))
            if desicion == 2:
                print(f'Has huido, el {self.__personaje2.nombre} ha quedado atras\n')
                break
            self.resultado_ronda()

