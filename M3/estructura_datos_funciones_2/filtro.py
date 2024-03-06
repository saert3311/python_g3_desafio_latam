from sys import argv

#Validar que se ingreso un umbral
if len(argv) <2:
    print("Error: Debe ingresar un umbral")
    exit()

#Validar el metodo de filtrado sea menor o mayor, tomar en cuenta que si no se ingresa nada, el metodo por defecto es mayor

if len(argv) == 3 and argv[2] not in ['menor', 'mayor']:
    print("Lo sentimos, no es una operación válida")
    exit()

precios = {'Notebook': 700000,
 'Teclado': 25000,
 'Mouse': 12000,
 'Monitor': 250000,
 'Escritorio': 135000,
 'Tarjeta de Video': 1500000}


def filtrar_productos(precios, umbral, metodo='mayor'):
    '''
    Filtra los productos que esten dentro del umbral de precios
    '''
    if metodo == 'menor':
        return {producto: precio for producto, precio in precios.items() if precio <= umbral}
    else:
        return {producto: precio for producto, precio in precios.items() if precio >= umbral}


def imprimir_productos(productos, separador=', '):
    '''
    Devuelve los nombres de los productos
    '''
    return separador.join(productos.keys())
    
#Nos aseguramos si hay metodo no nos de error al llamar al indice
metodo = argv[2] if len(argv) == 3 else None
    
productos_filtrados = filtrar_productos(precios, int(argv[1]), metodo)

if metodo == 'menor':
    print(f'Los productos menores al umbral son: {imprimir_productos(productos_filtrados)}')
    exit()

print(f'Los productos mayores al umbral son: {imprimir_productos(productos_filtrados)}')