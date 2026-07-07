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

