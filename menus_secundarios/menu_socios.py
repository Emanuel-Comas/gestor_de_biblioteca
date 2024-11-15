from interfaces.interfazSocios import baseSocios

class mostrarMenuS:

    def mostrarMenuSocio():
        print   ("""
                Menu Socios.
                 
            1- Agregar socio.
            2- Eliminar socio.
            3- Actualizar socio.
            4- Mostrar socios en base.
                """)
        
        valor = int(input("Elija una opcion: "))

        match valor:
            
            case 1:
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                fechaNac = input("Ingrese la fecha de nacimiento: ")
                direc = input("Ingrese la direccion: ")
                correo = input("Ingrese el correo: ")
                telefono = int(input("Ingrese el telefono: "))

                baseSocios.agregarSocios(nombre, apellido, fechaNac, direc, correo, telefono)

            case 2:
                baseSocios.eliminarSocios()

            case 3:
                baseSocios.updateSocios()

            case 4:
                baseSocios.mostrarSociosEnBase()
            
            case _:
                print("Error en menu de socio.")