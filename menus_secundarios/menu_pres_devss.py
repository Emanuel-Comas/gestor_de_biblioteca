from interfaces.interfazPreDev import basePrestamoDevo
from interfaces.interfazSocios import baseSocios
from interfaces.interfazLibros import baseLibros

class MostrarprestamosDev:
    def MostrarMenuPreDevv():
        
        print   ("""
                    Menu prestamos y
                    devoluciones.

                1- Agregar prestamo.
                2- Mostrar prestamos y devoluciones en base.
                """)
        
        valor = int(input("Elija una opcion: "))
        match valor:
            case 1:
                fechaPres = input("Ingrese fecha de prestamo: ")
                costo = input("Ingrese costo del prestamo: ")
                fechaDev = input("Ingrese fecha de devolucion: ")
                estadoPres = input("Ingrese estado del prestamo: ")
                idDelSocio = input("Ingrese el id del socio: ")
                idDelLibro = input("Ingrese el id del libro: ")

                # Variable para usar los datos del json
                ValidarSocioId = baseSocios.cargarSocios()
                ValidarLibroId = baseLibros.cargarLibros()

                for valorS in ValidarSocioId:
                    # "mostrarID()", se usa para acceder al atributo priv "__id".
                    if valorS.mostrarID() == idDelSocio:
                        print("Usuario encontrado.")

                        for valorL in ValidarLibroId:
                            if valorL.mostrarId() == idDelLibro:
                                print("Libro encontrado.")
                                basePrestamoDevo.agregarPrestamoDev(fechaPres, costo, fechaDev, estadoPres, idDelSocio, idDelLibro)
                                print("Base de prestamos/devoluciones actualizada.")
                                break

                        else:
                            print("Libro no encontrado.")
                
                    else:
                        print("Socio no encontrado, registrelo.")

            case 2:
                basePrestamoDevo.mostrarPresmosDevs()

            case _:
                print("Error en menu de prestamos y devoluciones.")
