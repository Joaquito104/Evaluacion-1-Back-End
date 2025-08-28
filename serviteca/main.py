from autos.gestion_autos import menu_autos
from clientes.gestion_clientes import menu_clientes
from servicios.gestion_servicios import menu_servicios

def crear_state():
    return {
        "autos": [],        # {"id", "nombre", "modelo", "anio"}
        "clientes": [],     # {"id", "nombre"}
        "servicios": [],    # {"id", "auto_id", "descripcion", "fecha?"}
        "counters": {"auto": 0, "cliente": 0, "servicio": 0}
    }

def main():
    state = crear_state()

    while True:
        print("\n=== SERVITECA ===")
        print("1. Gestión de Autos")
        print("2. Gestión de Clientes")
        print("3. Gestión de Servicios")
        print("4. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            menu_autos(state)
        elif opcion == "2":
            menu_clientes(state)
        elif opcion == "3":
            menu_servicios(state)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
