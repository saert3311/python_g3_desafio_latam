def choose_level(n_pregunta: int, p_level: int) -> str:
    
    # Construir lógica para escoger el nivel

    estado = n_pregunta / p_level

    if estado <= 1:
        return 'basicas'
    elif estado <= 2:
        return 'intermedias'
    else:
        return 'avanzadas'


if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias