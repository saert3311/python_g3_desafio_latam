from ingredientes import ingredientes, tipos_masa

class Pizza:
    NRO_MAX_INGREDIENTES = 3
    PROTEICOS = 1
    VEGETALES = 2

    def __init__(self):
        self.masa = None
        self.ingredientes = []
        self.pizza_valida = False

    def crear_pedido(self):
        ''' 
        Metodo para crear un pedido de pizza, valida el ingrediente y lo agrega al array 
        Igualmente para la masa
        Finalmente si el proceso se completa se cambia el valor de pizza_valida a True
        '''
        while len(self.ingredientes) < self.NRO_MAX_INGREDIENTES:
            if len(self.ingredientes) == 0: #el primer ingrediente es proteico por eso evaluamos si es 0 y saltamos los siguientes loops
                ingrediente = input(f'Ingresa el tipo de ingrediente proteico {ingredientes["proteicos"]}: ')
                if not self.validate_ingredientes(ingrediente, ingredientes['proteicos']):
                    print('El ingrediente ingresado no es válido')
                    continue
                self.ingredientes.append(ingrediente)
            ingrediente = input(f'Ingresa el tipo de ingrediente vegetal {ingredientes["vegetales"]}: ')
            if not self.validate_ingredientes(ingrediente, ingredientes['vegetales']):
                print('El ingrediente ingresado no es válido')
                continue
            self.ingredientes.append(ingrediente)
        while self.masa is None:
            masa = input(f'Ingresa el tipo de masa {tipos_masa}: ')
            if not self.validate_ingredientes(masa, tipos_masa):
                print('El tipo de masa ingresado no es válido')
                continue
            self.masa = masa
        self.pizza_valida = True #si completamos todo el proceso la pizza es valida

    @staticmethod
    def validate_ingredientes(ingrediente: str, ingredientes: list) -> bool:
        if ingrediente not in ingredientes:
            return False
        return True

    def __str__(self):
        return f'Pizza con masa {self.masa}\nIngredientes {self.ingredientes}\nLa Pizza {"es Valida" if self.pizza_valida else "No es válida"}'