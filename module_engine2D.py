class Engine2D:
    def __init__(self):
        self.canvas = []
        self.current_color = None

    def draw(self):
        for shape in self.canvas:
            shape.draw(self.current_color)
        self.canvas = []

    def set_color(self, color):
        self.current_color = color

    def add_shape(self, shape):
        self.canvas.append(shape)


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, color):
        raise NotImplementedError("Subclasses must implement the draw method.")


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self, color):
        return f"Drawing Circle: ({self.x}, {self.y}) with radius {self.radius} in {color}"


class Triangle(Shape):
    def __init__(self, x, y, side_length):
        super().__init__(x, y)
        self.side_length = side_length

    def draw(self, color):
        return f"Drawing Triangle: ({self.x}, {self.y}) with side length {self.side_length} in {color}"


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self, color):
        return f"Drawing Rectangle: ({self.x}, {self.y}) with width {self.width} and height {self.height} in {color}"
