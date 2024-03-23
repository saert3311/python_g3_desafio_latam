class Encuesta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__preguntas = []
        self.__respuestas = []

    def mostrar_encuesta(self):
        print(f'Encuesta: {self.nombre}')
        for i, pregunta in enumerate(self.__preguntas):
            print(f'{i+1}. {pregunta.mostar_pregunta}')

    def agregar_pregunta(self, pregunta):
        self.__preguntas.append(pregunta)

    def agregar_respuestas(self, respuestas):
        self.__respuestas.append(respuestas)

    def __str__(self):
        return f"Encuesta {self.nombre} con {len(self.preguntas)} preguntas"

EncuestaPorEdad(Encuesta):
    def __init__(self, nombre, edad_minima, edad_maxima):
        super().__init__(nombre)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

        def agregar_respuestas(self, respuestas):
            if self.edad_minima <= respuestas.usuario.edad <= self.edad_maxima:
                self.__respuestas.append(respuestas)
            else:
                print(f'{self.nombre} no es apta para la encuesta')

EncuestaPorRegion(Encuesta):
    def __init__(self, nombre, region):
        super().__init__(nombre)
        self.region = region

        def agregar_respuestas(self, respuestas):
            if respuestas.usuario.region == self.region:
                self.__respuestas.append(respuestas)
            else:
                print(f'{self.nombre} es de una region incorrecta')