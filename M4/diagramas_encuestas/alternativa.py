class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self.contenido = contenido
        self.ayuda = ayuda

    @property
    def contenido(self):
        return self.contenido
    
    @contenido.setter
    def contenido(self, contenido):
        self.contenido = contenido

    @property
    def ayuda(self):
        return self.ayuda

    @ayuda.setter
    def ayuda(self, ayuda):
        self.ayuda = ayuda

    def __str__(self):
        text = f'{self.contenido}'
        if self.ayuda is not None:
            text += f'Ayuda: ({self.ayuda})'
        return text