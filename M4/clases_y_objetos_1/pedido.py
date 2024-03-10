from te import Te

if __name__ == "__main__":
    tipo_te = input("Ingrese el tipo de Te: [1,2,3]")
    formato_te = input("Ingrese el tamaño de Te: [1,2]")

    print(Te.describir(tipo_te))
    print(Te.precio(formato_te))