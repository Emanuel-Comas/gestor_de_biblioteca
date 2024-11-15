import json
from socios import Socio
import os


class InterfazSocio:
    
    def __init__(self, sociosJjson):
        self.archivojson = sociosJjson
        self.sociosEnBase = self.cargarSocios()

    
    def cargarSocios(self):
        try:
            # Mientras este abierto "archivojson" en la variable "file"
            with open(self.archivojson, 'r') as file:
                Socios = json.load(file)
                return [Socio(**socio) for socio in Socios]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def guardarSocios(self):

        try:
            with open(self.archivojson, 'w') as fileSocios:
                json.dump([socioNuevo.to_dict() for socioNuevo in self.sociosEnBase], fileSocios, indent=4)
            print("json de Socios actualizado.")
        except Exception as e:
            print(f"Error al guardar el socio: {e}")   


    def agregarSocios(self, nombre, apellido , fechaNac, direc, correo ,telefono):
        #Creo la instancia 
        nuevoSocio = Socio(nombre, apellido , fechaNac, direc, correo ,telefono)

        self.sociosEnBase.append(nuevoSocio)
        self.guardarSocios()
        print(f"Socio agregado {nuevoSocio}")

    def eliminarSocios(self):
        valorBusqueda = input("Ingrese el ID del socio a borrar: ")

        for i in self.sociosEnBase:
            print(f"Comparando id busqueda: {valorBusqueda} con {i.id}")
            if i.id == valorBusqueda:
                self.sociosEnBase.remove(i)
                print(f"Se a eliminado {i}")
                # Actualizo la lista en "JSON"
                self.guardarSocios()
                break
            else:
                print("ID del socio no encontrado.")

    def updateSocios(self):

        valorBusqueda = input("Ingrese el ID del socio a actualizar/editar: ")

        for socio in self.sociosEnBase:
            try:
                if valorBusqueda == socio.id:
                    valor = int(input("Que desea actualizar/editar:"))
                    print("""}
                        
                        1- nombre. 
                        2- apellido. 
                        3- fecha de Nacimiento. 
                        4- dirección
                        5- correo. 
                        6- telefono
                        7- id.
                        """)
                    
                    match valor:
                        case 1:
                            nuevoNombre = input("Ingrese el nuevo nombre: ")
                            socio.nombre = nuevoNombre
                            print("Nombre actualizado.")
                            print(socio)
                            break
                        case 2:
                            nuevoApellido = input("Ingrese el nuevo apellido: ")
                            socio.apellido = nuevoApellido
                            print("Apellido actualizado.")
                            print(socio)
                            break
                        case 3:
                            nuevoFechaNac = input("Ingrese la nueva fecha de nacimiento: ")
                            socio.fechaNac = nuevoFechaNac
                            print("Fecha de nacimiento actualizada.")
                            print(socio)
                            break
                        case 4:
                            nuevoDirec = input("Ingrese el nuevo año de publicación: ")
                            socio.direc = nuevoDirec
                            print("Direccion actualizada.")
                            print(socio)
                            break
                        case 5:
                            nuevoCorreo = input("Ingrese el nuevo correo: ")
                            socio.correo = nuevoCorreo
                            print("correo actualizado.")
                            print(socio)
                            break
                        case 6:
                            nuevoTelefono = input("Ingrese telefono nuevo: ")
                            socio.telefono = nuevoTelefono
                            print("telefono actualizado.")
                            print(socio)
                            break
                        case 7:
                            nuevoId = input("Ingrese el id: ")
                            socio.id = nuevoId
                            print("Id del socio actualizado.")
                            print(socio)
                            break

                        case _:
                            print("Opcion no valida")

            except Exception as e:
                return f' Ocurrio un error: {e}'


        self.guardarSocios()



    def mostrarSociosEnBase(self):
        if not self.SociosEnBase:
            print("No hay socios en la base.")
        else:
            print("Socios actuales en la base de datos:")
            for socio in self.SociosEnBase:
                print(socio)
            

                
# Creo el "JSON"
baseSocios = InterfazSocio('Json_files/Socios.json')
if not os.path.exists('Json_files'):
    os.makedirs('Json_files')