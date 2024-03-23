class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero
    #agregamos para imprimir mas comodamente la instancia
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellidos}'