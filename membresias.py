from almacenamiento import cargar_clientes, guardar_clientes
from datetime import datetime, timedelta

def registrar_membresia():
    clientes = cargar_clientes()

    print("\n--- REGISTRAR MEMBRESÍA ---")
    cedula = input("Ingrese la cédula del cliente: ")

    for cliente in clientes:
        if cliente["cedula"] == cedula:
            print("Tipos de membresía:")
            print("1. Mensual")
            print("2. Trimestral")
            print("3. Anual")

            opcion = input("Seleccione una opción: ")

            fecha_inicio = datetime.now()

            if opcion == "1":
                tipo = "Mensual"
                fecha_fin = fecha_inicio + timedelta(days=30)
            elif opcion == "2":
                tipo = "Trimestral"
                fecha_fin = fecha_inicio + timedelta(days=90)
            elif opcion == "3":
                tipo = "Anual"
                fecha_fin = fecha_inicio + timedelta(days=365)
            else:
                print("Opción no válida.")
                return

            cliente["membresia"] = tipo
            cliente["estado"] = "Activo"
            cliente["fecha_inicio"] = fecha_inicio.strftime("%Y-%m-%d")
            cliente["fecha_fin"] = fecha_fin.strftime("%Y-%m-%d")

            guardar_clientes(clientes)
            print("Membresía registrada correctamente.")
            return

    print("Cliente no encontrado.")

def renovar_membresia():
    registrar_membresia()

def consultar_membresias():
    clientes = cargar_clientes()

    print("\n--- MEMBRESÍAS REGISTRADAS ---")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print("-----------------------------")
        print("Nombre:", cliente["nombre"])
        print("Cédula:", cliente["cedula"])
        print("Membresía:", cliente["membresia"])
        print("Estado:", cliente["estado"])

        if "fecha_inicio" in cliente:
            print("Fecha inicio:", cliente["fecha_inicio"])
            print("Fecha fin:", cliente["fecha_fin"])
