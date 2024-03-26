from error import LargoExcedidoError
from Anuncio import *
class Campana:
    def __init__(self, nombre: str, fecha_inicio, fecha_fin):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__anuncios = []

    #funcion para clasificar los anuncios contenidos en la lista segun su clase
    def clasificar_anuncios(self):
        clasificacion = {}
        for anuncio in self.__anuncios:
            if anuncio.__class__.__name__ not in clasificacion:
                clasificacion[anuncio.__class__.__name__] = 1
            else:
                clasificacion[anuncio.__class__.__name__] += 1
        return clasificacion

    @property
    def anuncios(self):
        return self.__anuncios

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        if len(nombre) > 250:
            raise LargoExcedidoError(len(nombre))
        self.__nombre = nombre

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    @property
    def fecha_fin(self):
        return self.__fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, fecha_fin):
        self.__fecha_fin = fecha_fin

    def agregar_anuncio(self, tipo, **kwargs):
        #crear un nuevo anuncio segun el tipo, los argumentos y agregarlo a la lista de anuncios
        match tipo.lower():
            case 'video':
                anuncio = AnuncioVideo(**kwargs)
            case 'display':
                anuncio = AnuncioDisplay(**kwargs)
            case 'social':
                anuncio = AnuncioSocial(**kwargs)
            case _:
                raise ValueError(f'{tipo} no es un tipo de anuncio válido')
        self.__anuncios.append(anuncio)

    def __str__(self) -> str:
        msj = f"Nombre de la Campana: {self.__nombre}\nAnuncios:"

        for key, value in self.clasificar_anuncios().items():
            msj += f"\n{key}: {value} "

        return msj