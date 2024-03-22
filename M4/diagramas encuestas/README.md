```mermaid
graph LR
class Usuario {
  correo: string
  edad: number
  region: number

  modificarCorreo()
  modificarEdad()
  modificarRegion()
}

class Encuesta {
  nombre: string
  preguntas: Pregunta[]
  listadosRespuestas: ListadoRespuestas[]

  mostrarEncuesta()
  agregarListadoRespuestas(usuario: Usuario) /* Considera restricciones edad y region*/
}

class Pregunta {
  enunciado: string
  ayuda: string (optional)
  requerida: boolean
  alternativas: Alternativa[]

  mostrarPregunta()
}

class Alternativa {
  contenido: string
  ayuda: string (optional)

  mostrarAlternativa()
}

class ListadoRespuestas {
  usuario: Usuario
  respuestas: number[]
}

class Respuesta {
  valor: number
}

Usuario --> ListadoRespuestas
Encuesta --> Pregunta
Encuesta --> ListadoRespuestas
Pregunta --> Alternativa

ListadoRespuestas <-> Usuario : Esta asociado a
ListadoRespuestas --> Respuesta
```