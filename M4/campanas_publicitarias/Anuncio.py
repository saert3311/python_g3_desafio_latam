from abc import ABC, abstractmethod
import inspect
from error import SubTipoInvalidoError

class Anuncio(ABC):
    @classmethod
    def get_childclases(cls) -> list:
        return cls.__subclasses__()

    @staticmethod
    def mostrar_formatos():
        for subclase in Anuncio.get_childclases():
            print(subclase.__name__)
            print('===============')

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_click: str, sub_tipo: str):
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_click = url_click
        self.__sub_tipo = sub_tipo

    @property
    def url_archivo(self) -> str:
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, url_archivo: str):
        self.__url_archivo = url_archivo
    
    @property
    def url_click(self) -> str:
        return self.__url_click

    @url_click.setter
    def url_click(self, url_click: str):
        self.__url_click = url_click

    @property
    def sub_tipo(self) -> str:
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, sub_tipo: str):
        if sub_tipo not in self.SUBTIPOS:
            raise SubTipoInvalidoError(sub_tipo)
        self.__sub_tipo = sub_tipo

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
         pass

    def __str__(self) -> str:
        return f"Anuncio de tipo {self.__class__.__name__} - {self.__sub_tipo}"

class AnuncioVideo(Anuncio):
    SUBTIPOS = ('instream', 'outstream')

    def __init__(self, ancho:int, alto:int, url_archivo:str, url_click:str, sub_tipo:str, duracion:int):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)
        self.__ancho = 1
        self.__alto = 1
        self.__duracion = duracion if duracion > 0 else 5
    
    @property
    def duracion(self) -> int:
        return self.__duracion

    @duracion.setter
    def duracion(self, duracion: int):
        self.__duracion = duracion if duracion > 0 else 5

    def comprimir_anuncio(self):
        print('COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN')
    
    def redimensionar_anuncio(self):
        print('RECORTE DE VIDEO NO IMPLEMENTADO AÚN')

class AnuncioDisplay(Anuncio):
    SUBTIPOS = ('traducional', 'native')

    def __init__(self, ancho:int, alto:int, url_archivo:str, url_click:str, sub_tipo:str):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)

    def comprimir_anuncio(self):
        print('COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN')
    
    def redimensionar_anuncio(self):
        print('REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN')

class AnuncioSocial(Anuncio):
    SUBTIPOS = ('facebook', 'linkedin')

    def __init__(self, ancho:int, alto:int, url_archivo:str, url_click:str, sub_tipo:str):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)

    def comprimir_anuncio(self):
        print('COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN')
    
    def redimensionar_anuncio(self):
        print('REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN')