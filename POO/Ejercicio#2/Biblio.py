from datetime import datetime, timedelta

class Socio:
    def __init__(self, numero, nombre, direccion):
        self.numero = numero
        self.nombre = nombre
        self.direccion = direccion
        self.prestamos = []

    def __str__(self):
        return f"Socio {self.numero}: {self.nombre}, Dirección: {self.direccion}, Libros prestados: {len(self.prestamos)}"

class Libro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
        self.socio_prestamo = None

    def __str__(self):
        estado = "Disponible" if self.disponible else f"Prestado a Socio {self.socio_prestamo.numero}"
        return f"Libro {self.codigo}: {self.titulo} de {self.autor}, Estado: {estado}"

class Prestamo:
    def __init__(self, libro, socio):
        self.libro = libro
        self.socio = socio
        self.fecha = datetime.now()

    def __str__(self):
        return f"Prestamo de {self.libro.titulo} a {self.socio.nombre}, Fecha: {self.fecha}"

class Biblioteca:
    def __init__(self):
        self.socios = []
        self.libros = []
        self.prestamos = []

    def agregar_socio(self, numero, nombre, direccion):
        socio = Socio(numero, nombre, direccion)
        self.socios.append(socio)
        return socio

    def agregar_libro(self, codigo, titulo, autor):
        libro = Libro(codigo, titulo, autor)
        self.libros.append(libro)
        return libro

    def prestar_libro(self, libro, socio):
        if libro.disponible:
            libro.disponible = False
            libro.socio_prestamo = socio
            prestamo = Prestamo(libro, socio)
            socio.prestamos.append(prestamo)
            self.prestamos.append(prestamo)
            return prestamo
        else:
            return None

    def socios_con_mas_de_tres_prestamos(self):
        return filter(lambda socio: len(socio.prestamos) > 3, self.socios)

# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Agregar socios y libros
    socio1 = biblioteca.agregar_socio(1, "Juan Pérez", "Calle A")
    socio2 = biblioteca.agregar_socio(2, "María Rodríguez", "Calle B")

    libro1 = biblioteca.agregar_libro(101, "Python 101", "John Doe")
    libro2 = biblioteca.agregar_libro(102, "Data Science for Beginners", "Jane Smith")

    # Mostrar información inicial
    print("\nInformación inicial:")
    print(socio1)
    print(socio2)
    print(libro1)
    print(libro2)

    # Prestar libros
    prestamo1 = biblioteca.prestar_libro(libro1, socio1)
    prestamo2 = biblioteca.prestar_libro(libro2, socio2)

    # Mostrar información después de los préstamos
    print("\nInformación después de los préstamos:")
    print(socio1)
    print(socio2)
    print(libro1)
    print(libro2)
    print(prestamo1)
    print(prestamo2)

    # Mostrar socios con más de 3 libros prestados
    print("\nSocios con más de 3 libros prestados:")
    for socio in biblioteca.socios_con_mas_de_tres_prestamos():
        print(socio)
