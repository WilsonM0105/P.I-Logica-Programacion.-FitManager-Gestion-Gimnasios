from almacenamiento import cargar_clientes, cargar_pagos

def generar_reportes():
    clientes = cargar_clientes()
    pagos = cargar_pagos()

    total_clientes = len(clientes)
    clientes_activos = 0
    clientes_inactivos = 0
    total_recaudado = 0

    for cliente in clientes:
        if cliente["estado"] == "Activo":
            clientes_activos += 1
        else:
            clientes_inactivos += 1

    for pago in pagos:
        try:
            total_recaudado += float(pago["monto"])
        except:
            total_recaudado += 0

    print("\n--- REPORTES BÁSICOS ---")
    print("Total de clientes:", total_clientes)
    print("Clientes activos:", clientes_activos)
    print("Clientes inactivos:", clientes_inactivos)
    print("Total de pagos registrados:", len(pagos))
    print("Total recaudado: $", total_recaudado)