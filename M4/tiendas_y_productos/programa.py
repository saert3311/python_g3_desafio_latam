from producto import Producto
from tienda import Tienda
#Creamos una lista para almacenar las tiendas
TIENDAS = []
#Nos apollamos en un diccionario para definir los tipos de tiendas use flags para definir el comportamiento de cada tipo
TIPOS = {
    'restaurante':{
        'ignorar_stock': True,
        'reportar_stock': False,
    },
    'supermercado':{
        'poco_stock': 10,
    },
    'farmacia':{
        'reportar_stock': False,
        'envio_gratis': 15000,
    }
}

def main():
    """Programa principal
    """    
    while True:
        print("Bienvenido!! Elige la opcion que desees:")
        print("1. Crear tienda")
        print("2. Crear producto")
        print("3. Operar con tienda")
        print("0. Salir")
        seleccion = int(input("Seleccione una opción: "))
        match selecion:
            case 1:
                crear_tienda()
                print('--------------------------')
            case 2:
                crear_producto()
                print('--------------------------')
            case 3:
                operar_tienda()
                print('--------------------------')
            case 0:
                break
            case _:
                print("Opción inválida")


def crear_tienda():
    """Creacion de tienda y almacenamiento en la lista de tiendas
    """    
    nombre = input("Nombre de la tienda: ")
    tipo = input("Tipo de tienda (restaurante, supermercado, farmacia): ")
    costo_delivery = int(input("Costo de delivery: "))
    if tipo in TIPOS:
        tienda = Tienda(nombre, costo_delivery=costo_delivery, **TIPOS[tipo] )
    else:
        tienda = Tienda(nombre, tipo, costo_delivery=costo_delivery)

    TIENDAS.append(tienda)
    print(f"Tienda {tienda} creada")

def elegir_tienda():
    """Seleccion de tienda y la devolvemos
    """
    print("Elige una tienda:")
    for i, tienda in enumerate(TIENDAS):
        print(f"{i+1}. {tienda}")
    seleccion = int(input("Seleccione una opción: "))
    return TIENDAS[seleccion-1]

def crear_producto():
    """Creacion de producto y almacenamiento en la tienda seleccionada
    """
    if not TIENDAS:
        print("Primero debes crear una tienda")
        return
    tienda_elegida = elegir_tienda()
    nombre = input("Nombre del producto: ")
    precio = int(input("Precio del producto: "))
    stock = int(input("Stock del producto: "))
    producto = Producto(nombre, precio, stock)
    resultado = tienda_elegida.nuevo_producto(producto)
    if resultado:
        print(f"Producto {producto.nombre} creado")
    else:
        print(f"Ocurrio un error al crear el producto {producto.nombre}")

def operar_tienda():
    """Operaciones con la tienda seleccionada
    """
    if not TIENDAS:
        print("Primero debes crear una tienda")
        return
    tienda_elegida = elegir_tienda()
    print("Elige la opcion que desees:")
    print("1. Venta de producto")
    print("2. Agregar stock")
    print("3. Listar productos")
    seleccion = int(input("Seleccione una opción: "))
    match seleccion:
        case 1:
            venta_producto(tienda_elegida)
        case 2:
            agregar_stock(tienda_elegida)
        case 3:
            tienda_elegida.listar_productos()
        case _:
            print("Opción inválida")

def venta_producto(tienda, producto=None, cantidad=None):
    """Venta de producto
    """
    producto_vender = input('Que producto deseas vender:') if producto is None else producto
    producto_cant = int(input('Que cantidad deseas vender:')) if producto is None else producto
    resultado, restante = tienda.venta(producto_vender, producto_cant)
    match (resultado, restante):
        case (resultado, restante) if resultado == True and restante >= 0:
            return print(f'Producto vendido!')
        case (resultado, restante) if resultado == False and restante > 0:
            reintentar = input(f'Solo restan {restante} en stock, deseas comprarlos (s/n)?')
            if reintentar.lower() == 's':
                if venta_producto(tienda, producto_vender, restante):
                    return print(f'Producto vendido!')
                else:
                    return print(f'Producto no vendido, revise nuevamente')
            else:
                return print(f'Producto no vendido')
        case (resultado, restante) if resultado == False and restante == 0:
            return print(f'Producto no vendido, no hay stock')

def agregar_stock(tienda):
    """Agregar stock a un producto
    """
    if tienda.config['manejar_stock'] == False:
        print('La tienda no maneja stock')
        return
    producto_agregar = input('Que producto deseas agregar stock:')
    producto_cant = int(input('Que cantidad deseas agregar:'))
    resultado = tienda.agregar_stock(producto_agregar, producto_cant)
    if resultado:
        print(f"Stock de {producto_agregar} aumentado en {producto_cant}")
    else:
        print(f"Ocurrio un error al aumentar el stock de {producto_agregar}")



if __name__ == "__main__":
    main()
