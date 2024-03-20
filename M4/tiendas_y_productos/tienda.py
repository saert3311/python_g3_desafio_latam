class Tienda:
    """Clase para instanciar una tienda
         
    """    
    def __init__(self, nombre, tipo, costo_delivery=0, manejar_stock=True, reportar_stock=True, envio_gratis=0, poco_stock=0):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []
        self.__manejar_stock = manejar_stock
        self.__reportar_stock = reportar_stock
        self.__envio_gratis = envio_gratis
        self.__poco_stock = poco_stock

    def __str__(self):
        return f"{self.nombre}"
    
    def nuevo_producto(self, producto):
        if not self.__manejar_stock:
            producto.ignorar_stock = True
        if producto not in self.__productos:
            self.__productos.append(producto)
            return True
        product_index = self.__productos.index(producto)
        self.__productos[product_index] += producto
        return True
    
    def venta(self, producto, cantidad):
        if producto in self.__productos:
            product_index = self.__productos.index(producto)
            return self.__productos[product_index].venta(cantidad)
        return False

    @property
    def nombre(self):
        return self.__nombre

    @property
    def tipo(self):
        return self._tipo

    @property
    def config(self):
        return {
            'costo_delivery': self.__costo_delivery,
            'manejar_stock': self.__manejar_stock,
            'reportar_stock': self.__reportar_stock,
            'envio_gratis': self.__envio_gratis,
            'poco_stock': self.__poco_stock
        }
    
    def listar_productos(self):
        print(f"Productos de {self.__nombre}:")
        for producto in self.__productos:
            msj = f'{producto.nombre}: {producto.precio}'
            if self.__reportar_stock:
                msj += f' - Stock: {producto.stock}'
            if producto.stock <= self.__poco_stock and self.__poco_stock != 0:
                msj += ' - “Pocos productos disponibles”'
            if producto.precio >= self.__envio_gratis and self.__envio_gratis != 0:
                msj += ' - “Envío gratis al solicitar este producto'
            print(msj)

    def agregar_stock(self, producto, cantidad):
        if producto in self.__productos:
            product_index = self.__productos.index(producto)
            self.__productos[product_index].reabastecer(cantidad)
            return True
        return False