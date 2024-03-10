class Te:
    """Una clase para representar un Te

    Returns:
        Objeto: Te
    """    
    SABORES = {
        "1": {"nombre": "Te Negro", "preparacion": "3 minutos", 'consumo': 'Desayuno'},
        "2": {"nombre": "Te Verde", "preparacion": "5 minutos", 'consumo': 'Medio dia'},
        "3": {"nombre": "Infusion de Hierbas", "preparacion": "6 minutos", 'consumo': 'Atardecer'},
    }
    PRESENTACIONES = {
        "1": {"peso": "300", "valor": "3000"},
        "2": {"peso": "500", "valor": "5000"},
    }

    ID = 0

    def __init__(self):
        Te.ID += 1
        self.identificador = Te.ID

    def __str__(self):
        return f'Objeto Te nro {self.identificador}'

    @staticmethod
    def describir(tipo):
        return f'El {Te.SABORES[tipo]["nombre"]} tiene un tiempo de preparacion de {Te.SABORES[tipo]["preparacion"]}, se recomienda consumir al {Te.SABORES[tipo]["consumo"]}'

    @staticmethod
    def precio(formato):
        return f'El precio correspondiente al formato de {Te.PRESENTACIONES[formato]["peso"]} es: {Te.PRESENTACIONES[formato]["valor"]}'