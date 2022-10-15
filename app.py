
#Programación orienta a objetos
#Objetos son aquello que tienen propiedad y métodos

#Clases

class Reservaciones:
    def __init__(self, nombre, fecha, evento):
        self.nombre = nombre
        self.fecha = fecha
        self.evento = evento
    
    def serialize(self):
        retorno = {
            "nombre": self.nombre,
            "fecha": self.fecha,
            "evento": self.evento
        }
        return retorno
    
class Aulas(Reservaciones):
    def __init__(self, identificacion, capacidad, nombre, fecha, evento):
        self.identificacion = identificacion
        self.capacidad = capacidad
        super().__init__(nombre, fecha, evento) ##Propiedad Heredadas

    def serialize2(self):
        retorno = {
            "identificación":self.identificacion,
            "capacidad": self.capacidad,
        }
        return retorno

class Equipos(Reservaciones):
    def __init__(self, equipo, matenimiento, nombre, fecha, evento):
        self.equipo = equipo
        self.matenimiento = matenimiento
        super().__init__(nombre, fecha, evento) ##Propiedad Heredadas



reservacion1 = Reservaciones("Antonio", "5-sep-2023", "clases de programación")
reservacion2 = Reservaciones("Mónica", "4-sep-2024", "concierto")
reservacion3 = Aulas("0110", 250, "Mónica", "4-sep-2024", "concierto")

print(reservacion1.serialize())
print(reservacion2.serialize())
print(reservacion3.serialize2(), reservacion3.serialize())
    
