class SubTipoInvalidoError(Exception):
    def __init__(self, subtipo):
        self.subtipo = subtipo

    def __str__(self):
        return f"El subtipo {self.subtipo} no es válido."

class LargoExcedidoError(Exception):
    def __init__(self, largo,):
        self.largo = largo

    def __str__(self):
        return f"{self.largo} excede el máximo permitido de caracteres."