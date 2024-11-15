import uuid

class PreDev:


    def __init__(self, fechaPres, costo, fechaDev, estadoPres, idDelSocio, idDelLibro, id = None):
        self.fechaPres = fechaPres
        self.costo = costo
        self.fechaDev = fechaDev
        self.estadoPres = estadoPres
        if id is None:
            self.__id = str(uuid.uuid4())
        else:
            self.__id = id
        self.idDelSocio = idDelSocio
        self.idDelLibro = idDelLibro

    def establecerfechaPres(self, fechaPres):
        self.fechaPres = fechaPres

    def establecerfechaPres(self, costo):
        self.costo = costo

    def establecerfechaPres(self, fechaDev):
        self.fechaDev = fechaDev

    def establecerfechaPres(self, estadoPres):
        self.estadoPres = estadoPres

    def establecerID(self, __id):
        self.__id = __id

    def mostrarID(self):
        return self.__id
    
    def establecerIdDelSocio(self, idDelSocio):
        self.idDelSocio = idDelSocio

    def establecerIdDelLibro(self, idDelLibro):
        self.idDelLibro = idDelLibro

    def to_dict(self):
        return {
            'fechaPres' : self.fechaPres,
            'costo' : self.costo,
            'fechaDev' : self.fechaDev,
            'estadoPres' : self.estadoPres,
            'id' : self.mostrarID(),
            'idDelSocio' : self.idDelSocio,
            'idDelLibro' : self.idDelLibro
        }
    

    def __str__(self):
        return f'\n Fecha de prestamo: {self.fechaPres}, \n Costo: {self.costo}, \n Fecha de devolución: {self.fechaDev}, \n Estado del prestamo: {self.estadoPres}, \n id: {self.mostrarID()}, \n idDelSocio: {self.idDelSocio}, \n idDelLibro: {self.idDelLibro}'
    


# Test
# prestamo1 = PreDev("11/11/2024", "u$s2500", "12/11/2024", "En curso")
# print(prestamo1)
