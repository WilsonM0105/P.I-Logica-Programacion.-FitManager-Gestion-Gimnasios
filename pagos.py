from almacenamiento import cargar_clientes, cargar_pagos, guardar_pagos
from datetime import datetime

def registrar_pago():
    clientes = cargar_clientes()
    pagos = cargar_pagos()

    print("\n--- REGISTRAR PAGO ---")
    cedula = input("Ingrese la cédula del cliente: ")

    cliente_encontrado = None

    for cliente in clientes:
        if cliente["cedula"] == cedula:
            cliente_encontrado = cliente

    if cliente_encontrado == None:
        print("Cliente no encontrado.")
        return

    monto = input("Ingrese el monto pagado: ")
    concepto = input("Concepto del pago: ")

    pago = {
        "cedula": cedula,
        "nombre": cliente_encontrado["nombre"],
        "monto": monto,
        "concepto": concepto,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    pagos.append(pago)
    guardar_pagos(pagos)

    print("Pago registrado correctamente.")

def consultar_historial_pagos():
    pagos = cargar_pagos()

    print("\n--- HISTORIAL DE PAGOS ---")

    if len(pagos) == 0:
        print("No existen pagos registrados.")
        return

    for pago in pagos:
        print("-----------------------------")
        print("Cliente:", pago["nombre"])
        print("Cédula:", pago["cedula"])
        print("Monto:", pago["monto"])
        print("Concepto:", pago["concepto"])
        print("Fecha:", pago["fecha"])
