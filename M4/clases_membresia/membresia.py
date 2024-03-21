# Importando
from abc import ABC, abstractmethod


class Membresia(ABC):
    '''
    Clase abstracta para definir el comportamiento de las membresias
    '''
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta

    @abstractmethod #nos aseguramos que las clases hijas implementen este método
    def cambiar_suscripcion(self, nueva_membresia: int):
        pass

    def __str__(self):
        return f'Membresia {type(self).__name__}'

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)


class Gratis(Membresia):
    '''
    Membresia mas basica
    '''
    costo = 0
    cantidad_dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia not in range(1, 6):
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)


class Basica(Membresia):
    costo = 3000
    cantidad_dispositivos = 2

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)

        if isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.__dias_regalo = 7

        elif isinstance(self, Pro):
            self.__dias_regalo = 15

    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia < 2 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)


class Familiar(Basica):
    costo = 5000
    cantidad_dispositivos = 5

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia not in [1, 3, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def modificar_control_parental(self):
        pass


class SinConexion(Basica):
    costo = 3500

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia not in [1, 2, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def incrementar_cantidad_maxima_offline(self):
        pass


class Pro(Familiar, SinConexion):
    costo = 7000
    cantidad_dispositivos = 6

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia < 1 or nueva_membresia > 3:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

if __name__ == "__main__":
    gratuita1 = Gratis("hola@email.com", "123 456 789")
    print(gratuita1)
    basica1 = gratuita1.cambiar_suscripcion(1)
    print(basica1)
    familiar1 = basica1.cambiar_suscripcion(2)
    print(familiar1)
    sin_conexion1 = familiar1.cambiar_suscripcion(3)
    print(sin_conexion1)
    pro1 = sin_conexion1.cambiar_suscripcion(4)
    print(pro1)
    gratuita2 = pro1.cancelar_suscripcion()
    print(gratuita2)

