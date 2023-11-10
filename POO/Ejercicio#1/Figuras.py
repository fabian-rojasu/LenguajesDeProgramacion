import math

# Clase base para objetos representables
class Drawable:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def draw(self):
        pass

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def get_position(self):
        return self._x, self._y

# Clase para representar texto
class Text(Drawable):
    def __init__(self, x, y, content):
        super().__init__(x, y)
        self._content = content

    def draw(self):
        print(f"Texto: {self._content} en la posición {self.get_position()}")

    def get_content(self):
        return self._content

    def set_content(self, content):
        self._content = content

# Clase para representar objetos geométricos
class Shape(Drawable):
    def draw(self):
        pass

# Clase para representar círculos
class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self._radius = radius

    def draw(self):
        print(f"Círculo de radio {self._radius} en la posición {self.get_position()}")

# Clase para representar elipses
class Ellipse(Shape):
    def __init__(self, x, y, major_axis, minor_axis):
        super().__init__(x, y)
        self._major_axis = major_axis
        self._minor_axis = minor_axis

    def draw(self):
        print(f"Elipse con ejes {self._major_axis} y {self._minor_axis} en la posición {self.get_position()}")

# Clase para representar rectángulos
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self._width = width
        self._height = height

    def draw(self):
        print(f"Rectángulo de dimensiones {self._width}x{self._height} en la posición {self.get_position()}")

# Clase para representar líneas
class Line(Shape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1)
        self._x2 = x2
        self._y2 = y2

    def draw(self):
        print(f"Línea desde {self.get_position()} hasta ({self._x2}, {self._y2})")

# Clase para representar cuadrados (hereda de Rectangle)
class Square(Rectangle):
    def __init__(self, x, y, side_length):
        super().__init__(x, y, side_length, side_length)

# Clase para representar grupos de objetos
class Group(Drawable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._objects = []

    def draw(self):
        print(f"Grupo en la posición {self.get_position()} con los siguientes objetos:")
        for obj in self._objects:
            obj.draw()

    def add_object(self, obj):
        self._objects.append(obj)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de diferentes elementos del editor gráfico de documentos
    text = Text(10, 20, "Hola, mundo!")
    circle = Circle(30, 40, 5)
    ellipse = Ellipse(50, 60, 8, 12)
    rectangle = Rectangle(70, 80, 15, 25)
    line = Line(90, 100, 110, 120)
    square = Square(130, 140, 10)

    # Crear un grupo y agregar elementos
    group = Group(0, 0)
    group.add_object(text)
    group.add_object(circle)
    group.add_object(ellipse)
    group.add_object(rectangle)
    group.add_object(line)
    group.add_object(square)

    # Dibujar los elementos
    group.draw()
