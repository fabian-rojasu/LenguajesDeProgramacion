from abc import ABC, abstractmethod


# Clase base para Contacto
class Contacto:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Teléfono: {self.telefono}"


# Clases concretas para Contacto (especializaciones)
class ContactoT1(Contacto):
    def __init__(self, nombre, apellido, telefono, atributo_t1):
        super().__init__(nombre, apellido, telefono)
        self.atributo_t1 = atributo_t1

    def __str__(self):
        return super().__str__() + f", Atributo T1: {self.atributo_t1}"


class ContactoT2(Contacto):
    def __init__(self, nombre, apellido, telefono, atributo_t2):
        super().__init__(nombre, apellido, telefono)
        self.atributo_t2 = atributo_t2

    def __str__(self):
        return super().__str__() + f", Atributo T2: {self.atributo_t2}"


# Clase base para Evento
class Evento:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha

    def __str__(self):
        return f"Evento: {self.nombre}, Fecha: {self.fecha}"


# Clases concretas para Evento (especializaciones)
class EventoT1(Evento):
    def __init__(self, nombre, fecha, atributo_evento_t1):
        super().__init__(nombre, fecha)
        self.atributo_evento_t1 = atributo_evento_t1

    def __str__(self):
        return super().__str__() + f", Atributo Evento T1: {self.atributo_evento_t1}"


class EventoT2(Evento):
    def __init__(self, nombre, fecha, atributo_evento_t2):
        super().__init__(nombre, fecha)
        self.atributo_evento_t2 = atributo_evento_t2

    def __str__(self):
        return super().__str__() + f", Atributo Evento T2: {self.atributo_evento_t2}"


# Patrón Abstract Factory para crear objetos de la agenda
class AgendaFactory(ABC):
    @abstractmethod
    def crear_contacto(self, nombre, apellido, telefono):
        pass

    @abstractmethod
    def crear_evento(self, nombre, fecha):
        pass


# Implementación de las fábricas concretas
class AgendaT1Factory(AgendaFactory):
    def crear_contacto(self, nombre, apellido, telefono):
        return ContactoT1(nombre, apellido, telefono, "AtributoT1")

    def crear_evento(self, nombre, fecha):
        return EventoT1(nombre, fecha, "AtributoEventoT1")


class AgendaT2Factory(AgendaFactory):
    def crear_contacto(self, nombre, apellido, telefono):
        return ContactoT2(nombre, apellido, telefono, "AtributoT2")

    def crear_evento(self, nombre, fecha):
        return EventoT2(nombre, fecha, "AtributoEventoT2")


# Patrón Singleton para la agenda
class AgendaSingleton:
    _instance = None

    def __new__(cls, factory):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.factory = factory
            cls._instance.contactos = []
            cls._instance.eventos = []
        return cls._instance

    def agregar_contacto(self, nombre, apellido, telefono):
        contacto = self.factory.crear_contacto(nombre, apellido, telefono)
        self.contactos.append(contacto)

    def agregar_evento(self, nombre, fecha):
        evento = self.factory.crear_evento(nombre, fecha)
        self.eventos.append(evento)

    def __str__(self):
        contactos_str = "\n".join(str(contacto) for contacto in self.contactos)
        eventos_str = "\n".join(str(evento) for evento in self.eventos)
        return f"\nContactos:\n{contactos_str}\nEventos:\n{eventos_str}"


# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de las fábricas concretas
    agenda_t1_factory = AgendaT1Factory()
    agenda_t2_factory = AgendaT2Factory()

    # Crear instancias de las agendas usando Singleton
    agenda_singleton_t1 = AgendaSingleton(agenda_t1_factory)
    agenda_singleton_t2 = AgendaSingleton(agenda_t2_factory)

    # Agregar contactos y eventos a las agendas
    agenda_singleton_t1.agregar_contacto("Juan", "Perez", "123456")
    agenda_singleton_t1.agregar_evento("EventoT1", "2023-01-01")

    agenda_singleton_t2.agregar_contacto("Maria", "Lopez", "789012")
    agenda_singleton_t2.agregar_evento("EventoT2", "2023-02-02")

    # Mostrar la información de las agendas
    print("Agenda 1:")
    print(agenda_singleton_t1)

    print("\nAgenda 2:")
    print(agenda_singleton_t2)


# Eager Singleton: La instancia se crea inmediatamente al cargar el módulo o al iniciar el programa, independientemente de si se necesita o no. 
# Puede consumir más recursos al inicio.

# Lazy Singleton: La instancia se crea solo cuando se solicita por primera vez. Puede ser más eficiente en términos de recursos, ya que la instancia se inicializa 
# solo cuando se necesita.

# Elección del tipo de Singleton:

# En este caso, el enfoque de Lazy Singleton es más adecuado ya que la instancia de la Agenda no se necesita hasta que se quiere agregar algo a la agenda. 
# Esto puede ayudar a mejorar el rendimiento inicial del programa. Sin embargo, la elección depende de los requisitos específicos del programa y las preferencias del desarrollador. 
# En este ejemplo, se ha implementado un Lazy Singleton.