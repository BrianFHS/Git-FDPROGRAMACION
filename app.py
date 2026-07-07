def mostrar_menu():
    print('''
    ====== MENU PRINCIPAL ======
      1. Stock por categoría
      2. B2. Buscar productos por rango de precio
      3. Actualizar precio
      4. Agregar producto
      5. Eliminar producto
      6. Mostrar productos
      7. Salir
    ===========================''')

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion >= 1 and opcion <= 7:
                return opcion
            else:
                print("Debe seleccionar una opción válida")

        except ValueError:
            print("Debe seleccionar una opción válida")


def leer_numero_mayor_cero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("Debe ser mayor que cero")
        except:
            print("Debe ingresar un número entero")


def leer_numero_cero_o_mayor(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero >= 0:
                return numero
            else:
                print("Debe ser mayor o igual a cero")
        except:
            print("Debe ingresar un número entero")


def buscar_codigo(codigo, productos):
    for cod in productos:
        if cod.lower() == codigo.lower():
            return True
    return False


def obtener_codigo(codigo, productos):
    for cod in productos:
        if cod.lower() == codigo.lower():
            return cod
    return ""


def validar_codigo(codigo, productos):
    if codigo.strip() == "":
        return False
    if buscar_codigo(codigo, productos):
        return False
    return True

def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    return True

def validar_categoria(categoria):
    if categoria.strip() == "":
        return False
    return True

def validar_precio(precio):
    if precio > 0:
        return True
    return False

def validar_disponible(opcion):
    if opcion.lower() == "s" or opcion.lower() == "n":
        return True
    return False

def validar_stock(stock):
    if stock >= 0:
        return True
    return False

def validar_vendidos(vendidos):
    if vendidos >= 0:
        return True
    return False

def stock_categoria(categoria, productos, inventario):
    total = 0

    for codigo in productos:
        if productos[codigo][1].lower() == categoria.lower():
            total = total + inventario[codigo][0]

    print("Stock total de la categoría:", total)

def buscar_precio(precio_min, precio_max, productos, inventario):
    lista = []

    for codigo in productos:
        precio = productos[codigo][2]
        stock = inventario[codigo][0]

        if precio >= precio_min and precio <= precio_max and stock > 0:
            nombre = productos[codigo][0]
            lista.append(nombre + "--" + codigo)

    lista.sort()

    if len(lista) == 0:
        print("No existen productos en ese rango")
    else:
        for producto in lista:
            print(producto)

def actualizar_precio(codigo, nuevo_precio, productos):
    codigo_real = obtener_codigo(codigo, productos)

    if codigo_real == "":
        return False
    else:
        productos[codigo_real][2] = nuevo_precio
        return True

def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    if buscar_codigo(codigo, productos):
        return False
    else:
        productos[codigo] = [nombre, categoria, precio, disponible]
        inventario[codigo] = [stock, vendidos]
        return True

def eliminar_producto(codigo, productos, inventario):
    codigo_real = obtener_codigo(codigo, productos)

    if codigo_real == "":
        return False
    else:
        del productos[codigo_real]
        del inventario[codigo_real]
        return True

def mostrar_productos(productos, inventario):
    for codigo in productos:
        print("CODIGO:", codigo)
        print("--------------------------")
        print("Nombre:", productos[codigo][0])
        print("Categoría:", productos[codigo][1])
        print("Precio: $" + str(productos[codigo][2]))
        print("Disponible:", productos[codigo][3])
        print("Stock:", inventario[codigo][0])
        print("Vendidos:", inventario[codigo][1])
        print("--------------------------")

def main():
    productos = {
        "P101": ["Cuaderno", "Papelería", 2490, True],
        "P102": ["Lápiz", "Papelería", 590, True],
        "P103": ["Botella", "Accesorios", 6990, False],
        "P104": ["Mochila", "Accesorios", 24990, True]
    }

    inventario = {
        "P101": [30, 15],
        "P102": [120, 50],
        "P103": [0, 10],
        "P104": [8, 25]
    }

    opcion = 0

    while opcion != 7:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            categoria = input("Ingrese categoría: ")
            stock_categoria(categoria, productos, inventario)

        elif opcion == 2:
            minimo = leer_numero_mayor_cero("Ingrese precio mínimo: ")
            maximo = leer_numero_mayor_cero("Ingrese precio máximo: ")
            buscar_precio(minimo, maximo, productos, inventario)

        elif opcion == 3:
            seguir = "s"

            while seguir.lower() == "s":
                codigo = input("Ingrese código: ")

                if buscar_codigo(codigo, productos):
                    precio = leer_numero_mayor_cero("Ingrese nuevo precio: ")

                    if actualizar_precio(codigo, precio, productos):
                        print("Precio actualizado")
                else:
                    print("Código inexistente")

                seguir = input("¿Desea continuar? s/n: ")

        elif opcion == 4:
            codigo = input("Ingrese código: ")
            while validar_codigo(codigo, productos) == False:
                print("Código inválido")
                codigo = input("Ingrese código: ")

            nombre = input("Ingrese nombre: ")
            while validar_nombre(nombre) == False:
                print("Nombre inválido")
                nombre = input("Ingrese nombre: ")

            categoria = input("Ingrese categoría: ")
            while validar_categoria(categoria) == False:
                print("Categoría inválida")
                categoria = input("Ingrese categoría: ")

            precio = leer_numero_mayor_cero("Ingrese precio: ")

            disponible_opcion = input("Disponible s/n: ")
            while validar_disponible(disponible_opcion) == False:
                print("Opción inválida")
                disponible_opcion = input("Disponible s/n: ")

            if disponible_opcion.lower() == "s":
                disponible = True
            else:
                disponible = False

            stock = leer_numero_cero_o_mayor("Ingrese stock: ")
            vendidos = leer_numero_cero_o_mayor("Ingrese vendidos: ")

            if agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
                print("Producto agregado")
            else:
                print("No se pudo agregar")

        elif opcion == 5:
            codigo = input("Ingrese código a eliminar: ")

            if eliminar_producto(codigo, productos, inventario):
                print("Producto eliminado")
            else:
                print("Código inexistente")

        elif opcion == 6:
            mostrar_productos(productos, inventario)

        elif opcion == 7:
            print("Programa finalizado")


main()