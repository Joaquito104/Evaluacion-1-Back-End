from autos.gestion_autos import menu_autos as autos
from clientes.gestion_clientes import menu_clientes as clientes
from servicios.gestion_servicios import menu_servicios as servicios

def menu_principal():
    while True:
        print("\n--- SERVITECA ---")
        print("1. Gestionar autos")
        print("2. Gestionar clientes")    
        print("3. Gestionar servicios")
        print("4. Salir")

        opcion = input('Elige una opcion:')

        match int(opcion):
            case 1 :
                autos()
            case 2 :
                clientes()
            case 3 :
                servicios()
            case 4:
                break

if __name__ == '__main__':
    menu_principal()