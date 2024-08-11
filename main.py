from os import system
def menu():
    while True:
        print("------------- MENU PRINCIPAL -------------")
        print("1. Registrar Auto")
        print("2. Registrar Cliente")
        print("3. Realizar Compra")
        print("4. Reporte de compras")
        print("5. Datos del Estudiantes")
        print("6. Salir")
        print("-------------------------------------------")
        opcion = int(input("Escribe la opcion que deseas: "))

        if opcion == 1:
            system("cls")
            print("Se ha regirstrado el auto")
        elif opcion == 2:
            system("cls")
            print("Se ha registrado el cliente")
        elif opcion == 3:
            system("cls")
            print("Se ha realizado una compra")
        elif opcion == 4:
            system("cls")
            print("Se ha realizado el informe de compras")
        elif opcion == 5:
            system("cls")
            print("Victor Andres Estrada Eguizabal")
            print("202001361")
            print("Introduccion a la Programacion y computacion 2 - Seccion: 'B' ")
            print("Ingenieria en Ciencias y Sistemas")
            print("4to Semestre")
        elif opcion == 6:
            system("cls")
            print("Saliendo del sistema")
            break
        else:
            print("Opcion no valida")
            print("Ingrese unicamente una de las opciones del menu principal")   

menu()