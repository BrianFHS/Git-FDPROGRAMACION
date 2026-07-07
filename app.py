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


