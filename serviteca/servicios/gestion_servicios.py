def menu_servicios(state):
    while True:
        print("\n--- GESTIÓN DE SERVICIOS ---")
        print("1. Agregar servicio")
        print("2. Listar servicios")
        print("3. Buscar servicios por auto (término)")
        print("4. Volver al menu principal")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            if not state["autos"]:
                print("No hay autos. Primero crea un auto.")
                continue

            _listar_autos_breve(state)
            auto_txt = input("Escribe el nombre/modelo/año del auto: ").strip()
            if not auto_txt:
                print("Debe escribir algo.")
                continue

            desc = input("Descripción del servicio: ").strip()
            if not desc:
                print("Debe ingresar una descripción.")
                continue

            fecha = input("Fecha (opcional): ").strip() or None
            s = crear_servicio(state, auto_txt, desc, fecha)
            print("Servicio registrado:", _fmt_servicio(s))

        elif opcion == "2":
            servicios = listar_servicios(state)
            if not servicios:
                print("No hay servicios registrados.")
            else:
                print("\nListado de servicios:")
                for s in servicios:
                    print(_fmt_servicio(s))

        elif opcion == "3":
            termino = input("Término (nombre/modelo/año): ").strip().lower()
            resultados = buscar_servicios(state, termino)
            if not resultados:
                print("No hay servicios para ese criterio.")
            else:
                print("\nServicios encontrados:")
                for s in resultados:
                    print(_fmt_servicio(s))

        elif opcion == "4":
            print("Volviendo al menu principal")
            break

        else:
            print("Opción no válida.")

def _next_id(state, kind):
    state["counters"][kind] += 1
    return state["counters"][kind]

def _fmt_auto(a: dict) -> str:
    return f"{a['nombre']} {a['modelo']} {a['anio']}"

def _listar_autos_breve(state):
    print("\nAutos disponibles:")
    for a in state["autos"]:
        print("  " + _fmt_auto(a))

def _fmt_servicio(s: dict) -> str:
    fecha = f" | Fecha: {s['fecha']}" if s.get("fecha") else ""
    return f"[{s['id']}] Auto: {s['auto']} | {s['descripcion']}{fecha}"

def crear_servicio(state, auto_txt: str, descripcion: str, fecha: str | None) -> dict:
    srv = {
        "id": _next_id(state, "servicio"),
        "auto": auto_txt,          #
        "descripcion": descripcion,
        "fecha": fecha
    }
    state["servicios"].append(srv)
    return srv

def listar_servicios(state) -> list:
    return state["servicios"]

def buscar_servicios(state, termino: str) -> list:
    return [s for s in state["servicios"] if termino in s["auto"].lower()]
