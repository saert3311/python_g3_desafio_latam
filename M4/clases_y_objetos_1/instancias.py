from te import Te

if __name__ == "__main__":
    te = Te()
    te2 = Te()

    tipo_dato_te = type(te)
    tipo_dato_te2 = type(te)
 
    #Tengo entendido ue comparar 2 objetos con el operador == compara las referencias de memoria y no los valores

    if te == te2:
        print("Son iguales")
    else:
        print("Son diferentes")