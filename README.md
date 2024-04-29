erDiagram
  PACIENTE ||--o{ CONSULTA : "tiene"
  MEDICO ||--o{ CONSULTA : "realiza"
  MEDICO ||--o{ LICENCIA : "entrega"
  PACIENTE ||--o{ LICENCIA : "recibe"
  ESPECIALIDAD ||--|{ MEDICO : "tiene"

  PACIENTE {
    rut PK
    nombre
    direccion
  }

  CONSULTA {
    id_consulta PK
    fecha
    hora_atencion
    numero_box
    rut_paciente FK
    rut_medico FK
  }

  MEDICO {
    rut PK
    nombre
    direccion
    cod_especialidad FK
  }

  LICENCIA {
    codigo PK
    diagnostico
    fecha_inicio
    fecha_termino
    rut_paciente FK
    rut_medico FK
  }

  ESPECIALIDAD {
    cod_especialidad PK
    descripcion
  }