import uuid

class Libro:

    def __init__(self, titulo, autor, editorial, anioPublic, genero, cantDisp, id = None):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anioPublic = anioPublic
        self.genero = genero
        self.cantDisp = cantDisp
        if id is None:
            self.__id = str(uuid.uuid4())
        else:
            self.__id = id

    # Metodos para modificar los atributos.

    def establecerTitulo(self, titulo):
        self.titulo = titulo

    def establecerAutor(self, autor):
        self.autor = autor

    def establecerEditorial(self, editorial):
        self.editorial = editorial

    def establecerAnioPublic(self, anioPublic):
        self.anioPublic = anioPublic

    def establecerGenero(self, genero):
        self.genero = genero

    def establecerCantDisp(self, cantDisp):
        self.cantDisp = cantDisp

    def establecerId(self, __id):
        self.__id = __id

    def mostrarId(self):
        return self.__id

    # "to_dict", para guardar/cargar en JSON.

    def to_dict(self):
        return {
            'titulo' : self.titulo,
            'autor' : self.autor,
            'editorial' : self.editorial,
            'anioPublic' : self.anioPublic,
            'genero' : self.genero,
            'cantDisp' : self.cantDisp,
            'id' : self.mostrarId()
        }
    
    def __str__(self) -> str:
        return f'\n Titulo: {self.titulo}\n Autor: {self.autor}\n Editorial: {self.editorial}\n Año de publicacion: {self.anioPublic}\n Género: {self.genero}\n Cantidad disponible: {self.cantDisp}, \n Id: {self.mostrarId()}'
    