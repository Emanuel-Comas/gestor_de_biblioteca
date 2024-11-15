import uuid

class Socio:

    def __init__(self, nombre, apellido , fechaNac, direc, correo ,telefono, id = None):
        self.nombre = nombre
        self.apellido = apellido
        self.fechaNac = fechaNac
        self.direc = direc
        self.correo = correo
        self.telefono = telefono
        if id is None:
            self.__id = str(uuid.uuid4())
        else:
            self.__id = id

    
    def establecerNombre(self, nombre):
        self.nombre = nombre

    def establecerNombre(self, apellido):
        self.apellido = apellido

    def establecerNombre(self, fechaNac):
        self.fechaNac = fechaNac

    def establecerNombre(self, direc):
        self.direc = direc

    def establecerNombre(self, correo):
        self.correo = correo

    def establecerNombre(self, telefono):
        self.telefono = telefono

    def establecerNuevoID(self, __id):
        self.__id = __id

    # Muestra el "ID" priv ya sea modificado o no.
    def mostrarID(self):
        return self.__id
    
    def to_dict(self):
        return {
            'nombre' : self.nombre,
            'apellido' : self.apellido,
            'fechaNac' : self.fechaNac,
            'direc' : self.direc,
            'correo' : self.correo,
            'telefono' : self.telefono,
            'id' : self.mostrarID()
        }


    def __str__(self):
        return f'\n Nombre: {self.nombre}, \n Apellido: {self.apellido}, \n Fecha de nacimiento: {self.fechaNac}, \n Dirección: {self.direc}, \n Correo: {self.correo}, \n teléfono: {self.telefono}, \n ID: {self.mostrarID()}'
    