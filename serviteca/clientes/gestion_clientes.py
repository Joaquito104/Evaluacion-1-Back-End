def menu_clientes(state):
    while True:
        print("\n--- GESTIÓN DE CLIENTES ---")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Volver al menu principal")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre completo: ").strip()
            if not nombre:
                print("Debe ingresar un nombre.")
                continue
            c = crear_cliente(state, nombre)
            print("Cliente agregado:", _fmt_cliente(c))

        elif opcion == "2":
            clientes = listar_clientes(state)
            if not clientes:
                print("No hay clientes.")
            else:
                print("\nListado de clientes:")
                for c in clientes:
                    print(_fmt_cliente(c))

        elif opcion == "3":
            term = input("Buscar por nombre/apellido: ").strip().lower()
            resultados = buscar_clientes(state, term)
            if not resultados:
                print("No se encontraron clientes.")
            else:
                print("\nResultados:")
                for c in resultados:
                    print(_fmt_cliente(c))

        elif opcion == "4":
            print("Volviendo...")
            break
        else:
            print("Opción no válida.")

def _next_id(state, kind):
    state["counters"][kind] += 1
    return state["counters"][kind]

def _fmt_cliente(c: dict) -> str:
    return f"[{c['id']}] {c['nombre']}"

def crear_cliente(state, nombre: str) -> dict:
    c = {"id": _next_id(state, "cliente"), "nombre": nombre}
    state["clientes"].append(c)
    return c

def listar_clientes(state) -> list:
    return state["clientes"]

def buscar_clientes(state, termino: str) -> list:
    return [c for c in state["clientes"] if termino in c["nombre"].lower()]

def obtener_cliente_por_id(state, cliente_id: int):
    return next((c for c in state["clientes"] if c["id"] == cliente_id), None)
