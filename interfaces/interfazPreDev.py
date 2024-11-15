import json
from prestamos_devoluciones import PreDev
import os

class PresDevs:

    def __init__(self, prestDevsJson):
        self.archivoJson = prestDevsJson
        self.pres_devBase = self.cargarPrestamosDev()

    
    def cargarPrestamosDev(self):
        try:
            with open(self.archivoJson, 'r') as file:
                datos = json.load(file)
                return [PreDev(**preDev) for preDev in datos]               
            
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def guardarprestamosDev(self):
        try:
            with open(self.archivoJson, 'w') as file:
                json.dump([preDevNuevo.to_dict() for preDevNuevo in self.pres_devBase], file, indent=4)
            print("Json devoluciones y prestamos, actualizado.")
        except Exception as e:
            print(f"Error al guardar: {e}")


    def agregarPrestamoDev(self, fechaPres, costo, fechaDev, estadoPres, idDelSocio, idDelLibro):

        # Creo uan instancia
        nuevoPrestDev = PreDev(fechaPres, costo, fechaDev, estadoPres, idDelSocio, idDelLibro)

        self.pres_devBase.append(nuevoPrestDev)
        self.guardarprestamosDev()
        print("Nuevo prestamo/devolucion guardada en la base.")
        print(f"Detalles: {nuevoPrestDev}")


    def mostrarPresmosDevs(self):
        print("Lista de prestamos en la base de datos.")
        for prestamos in self.pres_devBase:
            print(prestamos)

basePrestamoDevo = PresDevs('Json_files/PresDev.json')
if not os.path.exists('Json_files'):
    os.makedirs('Json_files')