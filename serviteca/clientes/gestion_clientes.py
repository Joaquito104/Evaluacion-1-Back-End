def menu_clientes():
    clientes = []

    while True:
        print("\n--- GESTIÓN DE CLIENTES ---")
        print("1. Agregar cliente")
        print("2. Listar clientes")    
        print("3. Buscar cliente")
        print("4. Volver al menú principal")

        opcion = input('Elige una opcion: ')

        if opcion == "1":
            cliente = input("Ingrese nombre completo: ")
            clientes.append(cliente)
            print("Cliente agregado.") 

        elif opcion == "2":
            if clientes:
                print("\nLista clientes\n")
                for i, cliente in enumerate(clientes, 1):
                    print(f"{i}. {cliente}")
            else:
                print("No hay clientes registrados.")

        elif opcion == "3":
            buscar = input("Ingrese nombre a buscar: ")
            resultados = []

            for cliente in clientes:
                if buscar.lower() in cliente.lower():
                    resultados.append(cliente)
            
            if resultados:
                print("\nClientes encontrados\n")
                for cliente in resultados:
                    print(cliente)
            else:
                print("No se encontraron clientes.")

        elif opcion == "4":
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida.")



