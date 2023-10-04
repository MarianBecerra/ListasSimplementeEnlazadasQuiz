class Persona:
    def __init__(self, cedula,nombre):
        self.cedula=cedula
        self.nombre=nombre
        self.siguiente=None

class Habitacion:
    def __init__(self, numero,huesped=None):
        self.numero=numero
        self.persona=huesped

class Lista:
    def __init__(self):
        self.cabeza=None
    
    def registro(self,cedula,nombre):
        nueva_persona=Persona(cedula,nombre)
        if self.cabeza is None:
            self.cabeza=nueva_persona
            return
        persona_actual=self.cabeza
        while(persona_actual.siguiente):
            persona_actual=persona_actual.siguiente
        
        persona_actual.siguiente=nueva_persona
    
    def imprimir(self):
        persona_actual=self.cabeza
        while(persona_actual):
            print(persona_actual.nombre)
            persona_actual=persona_actual.siguiente

registro = Lista()
registro.registro(254589,"Pepito")
registro.registro(987451,"Juanito")
registro.registro(658947,"Fulanito")
registro.imprimir()
