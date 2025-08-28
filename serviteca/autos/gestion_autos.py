def menu_autos():
    autos = []  
    while True:
        print("\n--- GESTIÓN DE AUTOS ---")
        print("1. Agregar auto")
        print("2. Listar autos")
        print("3. Buscar auto")
        print("4. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            auto = input("Ingrese marca, modelo y año: ")
            autos.append(auto)
            print("Auto agregado.")

        elif opcion == "2":
            if autos:
                print("\nLista de autos\n")
                for i, auto in enumerate(autos, 1):
                    print(f"{i}. {auto}")
            else:
                print(" No hay autos registrados.")

        elif opcion == "3":
            buscar = input("Ingrese texto a buscar: ")
            resultados = []

            for auto in autos:  
                if buscar.lower() in auto.lower():  
                    resultados.append(auto)

            if resultados:
                print("\nAutos encontrados\n")
                for auto in resultados:
                    print(auto)
            else:
                print("No se encontró ningún auto.")

        elif opcion == "4":
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida.")
           




