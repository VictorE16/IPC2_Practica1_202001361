class Auto:
    def __init__(self, placa, marca, modelo, descripcion, precio_unitario):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario

    def __str__(self):
        return f"{self.placa}, {self.marca}, {self.modelo}, Q{self.precio_unitario}"


class Cliente:
    def __init__(self, nombre, correo_electronico, nit):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.nit = nit

    def __str__(self):
        return f"Nombre: {self.nombre}, NIT: {self.nit}"


class Compra:
    id_counter = 1

    def __init__(self, cliente):
        self.id = Compra.id_counter
        Compra.id_counter += 1
        self.cliente = cliente
        self.lista_productos = []
        self.costo_total = 0.0

    def agregar_auto(self, auto):
        self.lista_productos.append(auto)
        self.costo_total += auto.precio_unitario

    def __str__(self):
        autos_str = "\n".join([str(auto) for auto in self.lista_productos])
        return f"Compra ID: {self.id}\nCliente: {self.cliente}\nAutos:\n{autos_str}\nCosto Total: Q{self.costo_total}"


class SuperAutosGT:
    def __init__(self):
        self.autos = []
        self.clientes = []
        self.compras = []

    def registrar_auto(self):
        placa = input("Ingrese la placa del auto: ")
        marca = input("Ingrese la marca del auto: ")
        modelo = input("Ingrese el modelo del auto: ")
        descripcion = input("Ingrese la descripción del auto: ")
        precio_unitario = float(input("Ingrese el precio unitario del auto: "))
        auto = Auto(placa, marca, modelo, descripcion, precio_unitario)
        self.autos.append(auto)
        print("Auto registrado exitosamente.")

    def registrar_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        correo_electronico = input("Ingrese el correo electrónico del cliente: ")
        nit = input("Ingrese el NIT del cliente: ")
        cliente = Cliente(nombre, correo_electronico, nit)
        self.clientes.append(cliente)
        print("Cliente registrado exitosamente.")

    def realizar_compra(self):
        nit_cliente = input("Ingrese el NIT del cliente que realiza la compra: ")
        cliente = next((c for c in self.clientes if c.nit == nit_cliente), None)

        if cliente is None:
            print("Cliente no encontrado.")
            return

        compra = Compra(cliente)

        while True:
            print("\n--- Submenú de Compra ---")
            print("1. Agregar Auto")
            print("2. Terminar Compra y Generar Factura")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                placa_auto = input("Ingrese la placa del auto que desea comprar: ")
                auto = next((a for a in self.autos if a.placa == placa_auto), None)
                if auto is None:
                    print("Auto no encontrado.")
                else:
                    compra.agregar_auto(auto)
                    print(f"Auto {auto.marca} {auto.modelo} agregado a la compra.")
            elif opcion == "2":
                agregar_seguro = input("¿Desea agregar seguro al auto? (SI/NO): ").upper()
                if agregar_seguro == "SI":
                    compra.costo_total += compra.costo_total * 0.15
                self.compras.append(compra)
                print("Compra finalizada. Factura generada:")
                print(compra)
                break
            else:
                print("Opción no válida.")

    def reporte_compras(self):
        if not self.compras:
            print("No se han realizado compras.")
        else:
            print("\n--- Reporte de Compras ---")
            for compra in self.compras:
                print(compra)
                print("---------------------------")

    def datos_estudiante(self):
        nombre = "Victor Andres Estrada Eguizabal"  
        carnet = "202001361"        
        curso = "Introduccion a la Programacion y computacion 2"
        seccion = "B"
        carrera = "Ingenieria en Ciencias y Sistemas"
        semestre= "4to Semestre"
        print(f"Nombre: {nombre}\nCarnet: {carnet}\nCurso: {curso}\nSeccion: {seccion}\nCarrera: {carrera}\nSemestre: {semestre}")

    def menu_principal(self):
        while True:
            print("\n------------- Menú Principal -------------")
            print("1. Registrar Auto")
            print("2. Registrar Cliente")
            print("3. Realizar Compra")
            print("4. Reporte de Compras")
            print("5. Datos de Estudiante")
            print("6. Salir")
            print("-------------------------------------------")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_auto()
            elif opcion == "2":
                self.registrar_cliente()
            elif opcion == "3":
                self.realizar_compra()
            elif opcion == "4":
                self.reporte_compras()
            elif opcion == "5":
                self.datos_estudiante()
            elif opcion == "6":
                print("Saliendo del sistema.")
                break
            else:
                print("Opción no válida.")


sistema = SuperAutosGT()
sistema.menu_principal()