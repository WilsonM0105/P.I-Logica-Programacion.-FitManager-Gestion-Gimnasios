from almacenamiento import crear_archivos_si_no_existen
from clientes import registrar_cliente, mostrar_clientes, buscar_cliente, editar_cliente, eliminar_cliente
from membresias import registrar_membresia, renovar_membresia, consultar_membresias
from pagos import registrar_pago, consultar_historial_pagos
from reportes import generar_reportes

def mostrar_menu_principal():
    crear_archivos_si_no_existen()

    opcion = ""

    while opcion != "0":
        print("\n====================================")
        print("        FITMANAGER - GIMNASIO       ")
        print("====================================")
        print("1. Registrar cliente")
        print("2. Mostrar clientes")
        print("3. Buscar cliente")
        print("4. Editar cliente")
        print("5. Eliminar cliente")
        print("6. Registrar membresía")
        print("7. Renovar membresía")
        print("8. Consultar membresías")
        print("9. Registrar pago")
        print("10. Consultar historial de pagos")
        print("11. Ver reportes básicos")
        print("0. Salir")
        print("====================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            editar_cliente()
        elif opcion == "5":
            eliminar_cliente()
        elif opcion == "6":
            registrar_membresia()
        elif opcion == "7":
            renovar_membresia()
        elif opcion == "8":
            consultar_membresias()
        elif opcion == "9":
            registrar_pago()
        elif opcion == "10":
            consultar_historial_pagos()
        elif opcion == "11":
            generar_reportes()
        elif opcion == "0":
            print("Gracias por usar FitManager.")
        else:
            print("Opción no válida. Intente nuevamente.")

        if opcion != "0":
            input("\nPresione ENTER para continuar...")