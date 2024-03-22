```mermaid
classDiagram
  class Usuario {
    + correo: string // Public
    private edad: int  // Private
    private region: int // Private
    
    modificarCorreo(): void
    modificarEdad(): void // Access modifier may be needed based on implementation
    modificarRegion(): void // Access modifier may be needed based on implementation
  }
  
  class Encuesta {
    + nombre: string // Public
    private preguntas: Pregunta[]  // Private (encapsulation)
    private listadosRespuestas: ListadoRespuestas[]  // Private (encapsulation)
    
    mostrarEncuesta(): void
    agregarListadoRespuestas(usuario: Usuario): void // Consider restrictions
  }
  
  class Pregunta {
    + enunciado: string // Public
    + ayuda: string (optional) // Public
    + requerida: boolean // Public
    private alternativas: Alternativa[]  // Private (encapsulation)
    
    mostrarPregunta(): void
  }
  
  class Alternativa {
    + contenido: string // Public
    + ayuda: string (optional) // Public
    
    mostrarAlternativa(): void
  }
  
  class ListadoRespuestas {
    private usuario: Usuario  // Private (encapsulation)
    private respuestas: int[]  // Private (encapsulation)
  }
  
  class Respuesta {
    + valor: int // Public
  }
  
  Usuario <-> ListadoRespuestas
  Encuesta <-> Pregunta
  Encuesta <-> ListadoRespuestas
  Pregunta <-> Alternativa
  ListadoRespuestas <-> 1 Usuario
  ListadoRespuestas <-> Respuesta
```