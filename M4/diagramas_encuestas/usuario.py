class Usuario:
    def __init__(self, nombre, edad, correo, region):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.region = region

    '''
    Por cuestiones de tiempo para podernos poner al dia y como era opcional no implementamos en este caso la logica de agregar respuestas
    Hay muchas cosas para tomar en cuenta, como por ejemplo, que si un usuario ya respondio la encuesta no deberia poder responderla de nuevo
    Si se agrega una respuesta a un usuario que ya respondio la encuesta, se deberia sobreescribir la respuesta anterior
    Como relacionar las respuestas con las preguntas, etc.
    Usariamos algun identificador de cada pregunta para relacionar las respuestas con las preguntas?

    Relacionado a como funcionaria puede ser como hicimos anteriormente en el caso de los productos y ventas.

    '''

    def __str__(self):
        return self.nombre