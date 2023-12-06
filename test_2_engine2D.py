import pytest
from module_engine2D import Engine2D, Circle, Triangle, Rectangle


def test_engine_draw():
    engine = Engine2D()
    engine.add_shape(Circle(0, 1, 5))
    engine.add_shape(Triangle(2, 3, 4))
    engine.add_shape(Rectangle(1, 1, 3, 2))
    engine.draw()


def test_engine_set_color():
    engine = Engine2D()
    engine.set_color("red")
    assert engine.current_color == "red"


def test_engine_change_color_between_shapes():
    engine = Engine2D()
    engine.set_color("red")
    engine.add_shape(Circle(0, 0, 5))
    engine.set_color("blue")
    engine.add_shape(Triangle(2, 3, 4))
    engine.draw()
    assert len(engine.canvas) == 0


def test_shapes_draw():
    circle = Circle(0, 0, 5)
    assert circle.draw("blue") == "Drawing Circle: (0, 0) with radius 5 in blue"

    triangle = Triangle(2, 3, 4)
    assert triangle.draw("green") == "Drawing Triangle: (2, 3) with side length 4 in green"

    rectangle = Rectangle(1, 1, 3, 2)
    assert rectangle.draw("orange") == "Drawing Rectangle: (1, 1) with width 3 and height 2 in orange"


def test_engine_draw_with_colors():
    engine = Engine2D()
    engine.set_color("red")
    engine.add_shape(Circle(0, 0, 5))
    engine.set_color("blue")
    engine.add_shape(Triangle(2, 3, 4))
    engine.add_shape(Rectangle(1, 1, 3, 2))
    engine.draw()
    assert len(engine.canvas) == 0