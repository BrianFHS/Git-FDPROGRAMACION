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