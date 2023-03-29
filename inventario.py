print("Bienvenidos al programa de gestion de inventarios".center(60,"-"))
cantidad = []
productos = []
precio = []

while True:
    print("""
    (1) Añadir productos
    (2) Buscar productos
    (3) Modificar productos
    (4) Ver productos
    (5) Salir
    """)

    respuesta = int(input("Ingrese su opcion: "))
    if respuesta == 1:
        ac = int(input("Ingrese la cantidad de su producto: "))
        ap = input("Ingrese el nombre de su producto: ")
        apre = int(input("Ingrese el precio de su producto: "))

        cantidad.append(ac)
        productos.append(ap)
        precio.append(apre)
    elif respuesta == 2:
        buscador = input("Ingrese el nombre del producto que quiere buscar: ")
        posicion = productos.index(buscador)
        print("La cantidad del producto es: ", cantidad[posicion])
        print("El nombre del producto es: ", productos[posicion])
        print("El precio del producto es: ", precio[posicion])
    elif respuesta == 3:
        buscador = input("Ingrese el producto que quiera modificar: ")
        posicion = productos.index(buscador)
        ac = int(input("Ingrese la cantidad de su producto: "))
        apre = int(input("Ingrese el precio de su producto: "))
        cantidad[posicion] = ac
        productos[posicion] = ap
        precio[posicion] = apre
    elif respuesta == 4:
        print("La cantidad es: ", cantidad)
        print("El nombre del producto es: ", productos)
        print("El precio es: ", precio)
    else:
        break

