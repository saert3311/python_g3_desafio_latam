class Producto:
    """Clase Producto
    Representa un producto en una tienda con nombre, precio y stock.

        Methods
    -------
    venta(cantidad=""):
        Reduce stock del producto en la cantidad especificada.

    reabastecer(cantidad=""):
        Aumenta stock del producto en la cantidad especificada.
    """    
    def __init__(self, nombre, precio, stock=0, ignorar_stock=False):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__ignorar_stock = ignorar_stock

    def __str__(self):
        return f"{self.nombre}"

    def __eq__(self, otro):
        '''
        Comparamos si es objeto o si es texto igualmente
        '''
        if isinstance(otro, Producto):
            return self.nombre.lower() == otro.nombre.lower()
        elif isinstance(otro, str):
            return self.nombre.lower() == otro.lower()
        else:
            return False

    def __add__(self, otro):
        '''
        Sumamos el stock de dos productos
        '''
        if self.__ignorar_stock:
            return 0
        if isinstance(otro, Producto):
            return self.__stock + otro.__stock
        else:
            return False

    def __sub__(self, otro):
        '''
        Restamos el stock de dos productos
        '''
        if self.__ignorar_stock:
            return 0
        if isinstance(otro, Producto):
            return self.__stock - otro.__stock
        else:
            return False

    @property
    def ignorar_stock(self):
        return self.__ignorar_stock
    
    @ignorar_stock.setter
    def ignorar_stock(self, valor):
        if not isinstance(valor, bool):
            #Aqui iria un raise pero solo mostraremos mensajito
            print("Solo se acepta booleanos")
        self.__ignorar_stock = valor

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio
    
    @property
    def stock(self):
        return self.__stock

    def venta(self, cantidad):
        """Funcion para venta de productos

        Args:
            cantidad (int): Cantida de productos a vender

        Returns:
            bool: resultado de la venta
            int: nuevo stock
        """
        if self.__ignorar_stock:
            return True, 0        
        if cantidad > self.__stock:
            return False, self.__stock
        self.__stock -= cantidad
        return True, self.__stock
    
    def reabastecer(self, cantidad):
        """Funcion para reabastecer productos

        Args:
            cantidad (int): Cantida de productos a reabastecer

        Returns:
            int: Nuevo stock
        """
        if self.__ignorar_stock:
            return 0          
        self.__stock += cantidad
        return self.__stock
    
