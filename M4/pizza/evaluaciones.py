from pizza import Pizza

if __name__ == '__main__':
    #imprimiendo atributos de clase
    print('Atributos de clase:')
    print(vars(Pizza))
    #Validar
    es_valido = Pizza.validate_ingredientes('salsa de tomate', ["salsa de tomate", "salsa bbq"])

    print(f'El ingrediente es {"válido" if es_valido else "No es válido"}')

    #instanciando objeto

    una_pizza = Pizza()
    una_pizza.crear_pedido()

    #Imprimir objeto
    print(una_pizza)

    print(Pizza.pizza_valida)