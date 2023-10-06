class Persona:
    def __init__(self, cedula,nombre,habitacion):
        self.cedula=cedula
        self.nombre=nombre
        self.habitacion=habitacion
        self.siguiente=None

class Habitacion:
    def __init__(self, numero,huesped=None):
        self.numero=numero
        self.persona=huesped
        self.siguiente=None

class Lista:
    def __init__(self):
        self.cabeza=None
    
    def registroPersona(self,cedula,nombre,habitacion):
        nueva_persona=Persona(cedula,nombre, habitacion)
        if self.cabeza is None:
            self.cabeza=nueva_persona
            return
        persona_actual=self.cabeza
        while(persona_actual.siguiente):
            persona_actual=persona_actual.siguiente
        
        persona_actual.siguiente=nueva_persona

    def registroHuesped(self, numero,huesped):
        nueva_habitacion = Habitacion(numero,huesped)
        if self.cabeza is None:
            self.cabeza=nueva_habitacion
            return
        habitacion_actual=self.cabeza
        while(habitacion_actual.siguiente):
            habitacion_actual=habitacion_actual.siguiente
        
        habitacion_actual.siguiente=nueva_habitacion

    def imprimirPersona(self):
        persona_actual=self.cabeza
        while(persona_actual):
            print(persona_actual.nombre)
            persona_actual=persona_actual.siguiente
        print("\n")
    
    def imprimirHabitacion(self):
        habitacion_actual=self.cabeza
        while(habitacion_actual):
            if habitacion_actual.persona is None:
                print("La habitación "+ str(habitacion_actual.numero)+ " esta disponible")
            else: 
                print("En la habitación "+ str(habitacion_actual.numero)+" se hospeda el cliente: "+ str(habitacion_actual.persona))
            habitacion_actual=habitacion_actual.siguiente
        print("\n")
    
    def habitacionDisponible(self):
        habitacion_actual=self.cabeza
        while(habitacion_actual):
            if habitacion_actual.persona is None:
                print("Habitación "+ str(habitacion_actual.numero))
            habitacion_actual=habitacion_actual.siguiente
        print ("\n")
    
    def habitacionnoDisponible(self):
        habitacion_actual=self.cabeza
        while(habitacion_actual):
            if not habitacion_actual.persona is None:
                print("Habitación "+ str(habitacion_actual.numero))
            habitacion_actual=habitacion_actual.siguiente
        print ("\n")
    
    def consultaIndividual(self, nombre):
        persona_actual=self.cabeza
        while(persona_actual):
            if persona_actual.nombre is nombre: 
                print("Identificación: " + str(persona_actual.cedula)+"    Nombre Cliente: " + str(persona_actual.nombre)+ "    Habitación: "+ str(persona_actual.habitacion))
            persona_actual=persona_actual.siguiente
    
    def consultaCedula(self, cedula):
        persona_actual=self.cabeza
        persona_busqueda=persona_actual
        cont=0
        while(persona_actual):
            if persona_actual.cedula is cedula: 
                cont=cont+1
                persona_busqueda=persona_actual
            persona_actual=persona_actual.siguiente

        print("El cliente identificado con la cedula "+ str(persona_busqueda.cedula)+" ha estado registrado "+ str(cont)+ " veces")


registro = Lista()
registro.registroPersona(254589,"Pepito", 402)
registro.registroPersona(987451,"Juanito", 508)
registro.registroPersona(658947,"Fulanito",202)
registro.registroPersona(987451,"Juanito", 508)
registro.registroPersona(254589,"Pepito", 802)
registro.registroPersona(254589,"Pepito", 342)
registro.registroPersona(987451,"Juanito", 508)

print ("\n*****  LIBRO DE ENTRADAS  *****")
print("Las personas que se hospedan en el hotel son: ")
registro.imprimirPersona()

salida=Lista()
salida.registroPersona(894566,"Mariana", 506)
salida.registroPersona(543655,"Erick", 104)
salida.registroPersona(984524,"Sofia", 403)

print ("*****  LIBRO DE SALIDAS  *****")
print("La personas que salieron del hotel son: ")
salida.imprimirPersona()

habitaciones = Lista()
habitaciones.registroHuesped(404,"Pepito")
habitaciones.registroHuesped(205,"Juanito")
habitaciones.registroHuesped(502, None)

print ("*****  DISPONIBILIDAD DE HABITACIONES  *****\n")
print("La habitaciones del hotel son: ")
habitaciones.imprimirHabitacion()

print ("Las habitaciones disponibles son: ")
habitaciones.habitacionDisponible()

print("Las habitaciones no disponibles son: ")
habitaciones.habitacionnoDisponible()

print("El cliente Pepito se ha hospedado en: ")
registro.consultaIndividual("Pepito")

print ("\nLa busqueda del cliente arroja que: ")
registro.consultaCedula(987451)
registro.consultaCedula(254589)

print ("\nLos clientes por orden de llegada son: ")
registro.imprimirPersona()
