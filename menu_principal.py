from menus_secundarios.menu_libros import mostrarMenuL
from menus_secundarios.menu_socios import mostrarMenuS
from menus_secundarios.menu_pres_devss import MostrarprestamosDev


def main():
    print("""
                MENU
        1- Libros.
        2- Socios.
        3- Prestamos y devoluciones.
        """)

    opcion = int(input("Elija una opcion: "))

    match opcion:
        case 1:
            mostrarMenuL.mostrarMenuLibros()
        case 2:
            mostrarMenuS.mostrarMenuSocio()
        case 3:
            MostrarprestamosDev.MostrarMenuPreDevv()


# Llamo a la funcion principal.
if __name__ == '__main__':
    main()



   