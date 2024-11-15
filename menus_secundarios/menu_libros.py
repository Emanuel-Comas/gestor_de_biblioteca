
# Llamo al "JSON" que contendra/contiene los datos.
from interfaces.interfazLibros import baseLibros

class mostrarMenuL:

    def mostrarMenuLibros():
        print("""
                Menu Libros
            1- Agregar libro
            2- Eliminar libro
            3- Actualizar libro
            4- Mostrar libros en la base.
              """)
        
        opcion = int(input("Elija una opcion: "))

        match opcion:
            case 1:
                #Datos del libro a agregar.
                titulo = input("Ingrese el titulo: ")
                autor = input("Ingrese el autor: ")
                editorial = input("Ingrese el editorial: ")
                anioPublic = input("Ingrese el año de publicación: ")
                genero = input("Ingrese el genéro: ")
                cantDisp = input("Ingrese la cantidad disponible:")

                baseLibros.agregarLibro(titulo, autor, editorial, anioPublic, genero, cantDisp)
            
            case 2:
                baseLibros.eliminarLibro()

            case 3:
                baseLibros.updateLibro()

            case 4:
                baseLibros.mostrarLibrosEnBase()
            case _:
                print("Error de eleccion.")