class Personaje:
    '''
    Clase que representa a un personaje del juego Gran Fantasía
    '''
    JUGADORES_CREADOS = 0

    def __init__(self, nombre=None):
        self.__nivel = 1
        self.__experiencia = 0
        self.__experiencia_total = 0 #Esto lo uso para validar el nivel actual
        if nombre is None: #Para generar nombres facilmente jajaja
            Personaje.JUGADORES_CREADOS += 1
            self.__nombre = f'Jugador {Personaje.JUGADORES_CREADOS}'
        else:
            self.__nombre = nombre

    def __gt__(self, otro):
        return self.__nivel > otro.__nivel

    def __lt__(self, otro):
        return self.__nivel < otro.__nivel

    def __eq__(self, otro):
        return self.__nivel == otro.__nivel

    @property
    def nombre(self):
        return self.__nombre

    @property
    def nivel(self):
        return self.__nivel

    @property
    def experiencia(self):
        return self.__experiencia

    @property
    def estado(self):
        return f'Nombre: {self.__nombre}   Nivel: {self.__nivel}  Experiencia: {self.__experiencia}'

    def asumir_experiencia(self, experiencia):
        self.__experiencia += experiencia
        self.__experiencia_total += experiencia
        #Subir de nivel
        while self.__experiencia >= 100:
            self.__nivel += 1
            self.__experiencia -= 100
            print(f'{self.__nombre} ha subido de nivel a {self.__nivel}')
        #Desendiendo de nivel
        while self.__experiencia < 0:
            self.__nivel -= 1
            self.__experiencia += 100
            print(f'{self.__nombre} ha bajado de nivel a {self.__nivel}') if self.__nivel > 0 else print(f'{self.__nombre} ha bajado de nivel a 1')
        if self.__nivel  <= 0: #No queremos que la experiencia sea negativa
            self.__experiencia = 0
            self.__nivel = 1
        if self.__experiencia_total <= 0:
            self.__experiencia_total = 0


if __name__ == '__main__':
    #Pseudo tests
    jugador1 = Personaje()
    jugador1.asumir_experiencia(-30)
    print(jugador1.estado)
