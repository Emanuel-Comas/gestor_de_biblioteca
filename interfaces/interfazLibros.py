import json
from libros import Libro
import os


class InterfazLibros():
    
    def __init__(self, libritosJjson):
        self.archivojson = libritosJjson
        self.librosEnBase = self.cargarLibros()

    
    def cargarLibros(self):
        try:
            # Mientras este abierto "archivojson" en la variable "file"
            with open(self.archivojson, 'r') as file:
                Libritos = json.load(file)
                return [Libro(**libro) for libro in Libritos]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def guardarLibros(self):

        try:
            with open(self.archivojson, 'w') as fileLibro:
                json.dump([Libro.to_dict() for Libro in self.librosEnBase], fileLibro, indent=4)
            print("json de libros actualizado.")
        except Exception as e:
            print(f"Error al guardar el libro: {e}")   


    def agregarLibro(self, titulo, autor, editorial, anioPublic, genero, cantDisp):
        #Creo la instancia 
        nuevoLibro = Libro(titulo, autor, editorial, anioPublic, genero, cantDisp)

        self.librosEnBase.append(nuevoLibro)
        self.guardarLibros()
        print(f"Libro agregado {nuevoLibro}")

    def eliminarLibro(self):
        valorBusqueda = input("Ingrese el ID del libro a borrar: ")

        for i in self.librosEnBase:
            print(f"Comparando id busqueda: {valorBusqueda} con {i.id}")
            if i.id == valorBusqueda:
                self.librosEnBase.remove(i)
                print(f"Se a eliminado {i}")
                # Actualizo la lista en "JSON"
                self.guardarLibros()
                break
            else:
                print("ID no encontrado.")

    def updateLibro(self):

        valorBusqueda = input("Ingrese el ID del libro a actualizar/editar: ")

        for libro in self.librosEnBase:
            try:
                if valorBusqueda == libro.id:
                    valor = int(input("Que desea actualizar/editar:"))
                    print("""}
                        
                        1- titulo. 
                        2- autor. 
                        3- editorial. 
                        4- año de publicación. 
                        5- genéro. 
                        6- cantidad disponible.
                        7- id.
                        """)
                    
                    match valor:
                        case 1:
                            nuevoNombre = input("Ingrese el nuevo nombre: ")
                            libro.nombre = nuevoNombre
                            print("Nombre actualizado.")
                            print(libro)
                            break
                        case 2:
                            nuevoAutor = input("Ingrese el nuevo autor: ")
                            libro.autor = nuevoAutor
                            print("Autor actualizado.")
                            print(libro)
                            break
                        case 3:
                            nuevoEditorial = input("Ingrese el nuevo editorial: ")
                            libro.editorial = nuevoEditorial
                            print("Editorial actualizado.")
                            print(libro)
                            break
                        case 4:
                            nuevoAnioPublic = input("Ingrese el nuevo año de publicación: ")
                            libro.anioPublic = nuevoAnioPublic
                            print("año de publicación actualizado.")
                            print(libro)
                            break
                        case 5:
                            nuevoGenero = input("Ingrese el nuevo genéro: ")
                            libro.genero = nuevoGenero
                            print("genéro actualizado.")
                            print(libro)
                            break
                        case 6:
                            nuevocantDisp = input("Ingrese cantidad disponible: ")
                            libro.cantDisp = nuevocantDisp
                            print("cantidad disponible actualizado.")
                            print(libro)
                            break
                        case 7:
                            nuevoId = input("Ingrese el id: ")
                            libro.id = nuevoId
                            print("Id actualizado.")
                            print(libro)
                            break

                        case _:
                            print("Opcion no valida")

            except Exception as e:
                return f' Ocurrio un error: {e}'


        self.guardarLibros()



    def mostrarLibrosEnBase(self):
        # "libritos es en JSON".
        if not self.librosEnBase:
            print("No hay libros en la base.")
        else:
            print("Libros actuales en la base de datos:")
            for libro in self.librosEnBase:
                print(libro)
            

                
# Creo el "JSON"
baseLibros = InterfazLibros('Json_files/Libros.json')
if not os.path.exists('Json_files'):
    os.makedirs('Json_files')