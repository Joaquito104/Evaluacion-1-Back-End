def menu_autos(state):
    while True:
        print("\n--- GESTIÓN DE AUTOS ---")
        print("1. Agregar auto")
        print("2. Listar autos")
        print("3. Buscar auto")
        print("4. Volver")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre (marca): ").strip()
            modelo = input("Modelo: ").strip()
            anio = input("Año (ej: 2015): ").strip()

            if not nombre or not modelo or not anio.isdigit():
                print("Datos inválidos.")
                continue

            auto = crear_auto(state, nombre, modelo, int(anio))
            print("Auto agregado:", _fmt_auto(auto))

        elif opcion == "2":
            autos = listar_autos(state)
            if not autos:
                print("No hay autos registrados.")
            else:
                print("\nListado de autos:")
                for a in autos:
                    print(_fmt_auto(a))

        elif opcion == "3":
            term = input("Buscar por nombre/modelo/año: ").strip().lower()
            encontrados = buscar_autos(state, term)
            if not encontrados:
                print("No se encontraron autos.")
            else:
                print("\nResultados:")
                for a in encontrados:
                    print(_fmt_auto(a))

        elif opcion == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida.")


def _next_id(state, kind):
    state["counters"][kind] += 1
    return state["counters"][kind]

def _fmt_auto(a: dict) -> str:
    return f"[{a['id']}] {a['nombre']} {a['modelo']} {a['anio']}"

def crear_auto(state, nombre: str, modelo: str, anio: int) -> dict:
    auto = {"id": _next_id(state, "auto"), "nombre": nombre, "modelo": modelo, "anio": anio}
    state["autos"].append(auto)
    return auto

def listar_autos(state) -> list:
    return state["autos"]

def buscar_autos(state, termino: str) -> list:
    return [
        a for a in state["autos"]
        if termino in a["nombre"].lower()
        or termino in a["modelo"].lower()
        or termino in str(a["anio"]).lower()
    ]

def obtener_auto_por_id(state, auto_id: int):
    return next((a for a in state["autos"] if a["id"] == auto_id), None)
