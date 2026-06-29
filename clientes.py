from almacenamiento import cargar_clientes, guardar_clientes

def registrar_cliente():
    clientes = cargar_clientes()

    print("\n--- REGISTRAR CLIENTE ---")
    cedula = input("Cédula: ")

    for cliente in clientes:
        if cliente["cedula"] == cedula:
            print("Ya existe un cliente con esa cédula.")
            return

    nombre = input("Nombre completo: ")
    telefono = input("Teléfono: ")
    edad = input("Edad: ")

    nuevo_cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "edad": edad,
        "membresia": "Sin membresía",
        "estado": "Inactivo"
    }

    clientes.append(nuevo_cliente)
    guardar_clientes(clientes)

    print("Cliente registrado correctamente.")

def mostrar_clientes():
    clientes = cargar_clientes()

    print("\n--- CLIENTES REGISTRADOS ---")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print("-----------------------------")
        print("Cédula:", cliente["cedula"])
        print("Nombre:", cliente["nombre"])
        print("Teléfono:", cliente["telefono"])
        print("Edad:", cliente["edad"])
        print("Membresía:", cliente["membresia"])
        print("Estado:", cliente["estado"])

def buscar_cliente():
    clientes = cargar_clientes()

    print("\n--- BUSCAR CLIENTE ---")
    cedula = input("Ingrese la cédula del cliente: ")

    for cliente in clientes:
        if cliente["cedula"] == cedula:
            print("\nCliente encontrado:")
            print("Cédula:", cliente["cedula"])
            print("Nombre:", cliente["nombre"])
            print("Teléfono:", cliente["telefono"])
            print("Edad:", cliente["edad"])
            print("Membresía:", cliente["membresia"])
            print("Estado:", cliente["estado"])
            return

    print("Cliente no encontrado.")

def editar_cliente():
    clientes = cargar_clientes()

    print("\n--- EDITAR CLIENTE ---")
    cedula = input("Ingrese la cédula del cliente: ")

    for cliente in clientes:
        if cliente["cedula"] == cedula:
            print("Cliente encontrado. Deje vacío si no desea cambiar un dato.")

            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_telefono = input("Nuevo teléfono: ")
            nueva_edad = input("Nueva edad: ")

            if nuevo_nombre != "":
                cliente["nombre"] = nuevo_nombre

            if nuevo_telefono != "":
                cliente["telefono"] = nuevo_telefono

            if nueva_edad != "":
                cliente["edad"] = nueva_edad

            guardar_clientes(clientes)
            print("Cliente actualizado correctamente.")
            return

    print("Cliente no encontrado.")

def eliminar_cliente():
    clientes = cargar_clientes()

    print("\n--- ELIMINAR CLIENTE ---")
    cedula = input("Ingrese la cédula del cliente: ")

    for cliente in clientes:
        if cliente["cedula"] == cedula:
            clientes.remove(cliente)
            guardar_clientes(clientes)
            print("Cliente eliminado correctamente.")
            return

    print("Cliente no encontrado.")
