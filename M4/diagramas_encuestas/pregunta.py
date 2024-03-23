from alternativa import Alternativa

class Pregunta():
    def __init__(self, enunciado, ayuda=None, requerida=False):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.alternativas = []
    
    def agregar_alternativa(self, **kwargs):
        nueva_alternativa = Alternativa(**kwargs)
        self.alternativas.append(nueva_alternativa)

    @property
    def mostrar_pregunta(self):
        print(f'{self.enunciado}')
        if self.ayuda is not None:
            print(f'Ayuda: {self.ayuda}')
        for i, alternativa in enumerate(self.alternativas):
            print(f'{i+1}. {alternativa}')

    def __str__(self):
        return self.texto