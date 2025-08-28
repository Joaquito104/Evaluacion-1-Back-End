def menu_servicios():
    servicios = []  

    while True:
        print("\n--- GESTIÓN DE SERVICIOS ---")
        print("1. Agregar servicio")
        print("2. Listar servicios")    
        print("3. Buscar servicios por auto")
        print("4. Volver al menú principal")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            auto_txt = input("Auto (marca, modelo y año): ").strip()
            desc = input("Descripción del servicio: ").strip()

            if not auto_txt or not desc:
                print("Faltan datos.")
                continue
            servicios.append({"auto": auto_txt, "descripcion": desc})
            print("Servicio agregado.") 

        elif opcion == "2":
            if servicios:
                print("\nLista de servicios\n")
                for i, s in enumerate(servicios, 1):
                    print(f"{i}. Auto: {s['auto']} | Servicio: {s['descripcion']}")
            else:
                print("No hay servicios registrados.")

        elif opcion == "3":
            if not servicios:
                print("No hay servicios registrados.")
                continue

            criterio = input("Texto del auto a buscar: ").strip().lower()
            if not criterio:
                print("Búsqueda vacía.")
                continue


            encontrados = []  

            for s in servicios:
                if criterio in s["auto"].lower():
                    encontrados.append(s)

            if encontrados:
                print("\nServicios encontrados\n")
                for s in encontrados:
                    print(f"Auto: {s['auto']} | Servicio: {s['descripcion']}")
            else:
                print("No se encontraron servicios para ese auto.")

        elif opcion == "4":
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida.")

