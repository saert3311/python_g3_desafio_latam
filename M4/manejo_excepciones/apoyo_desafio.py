from error import DimensionError

class Foto():
    MAX = 2500

    @staticmethod
    def validar_dimension(dimension: int) -> None:
        #aqui podemos poner diferentes validaciones para tenerlas agrupadas
        if dimension > Foto.MAX:
            raise DimensionError("La dimensión de la foto excede el máximo permitido", "dimension", Foto.MAX)

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        self.validar_dimension(ancho)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        self.validar_dimension(alto)
        self.__alto = alto