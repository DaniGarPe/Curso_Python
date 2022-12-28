# A simple static factory method.
import random

class Shape(object):
    # Create based on class name:
    def factory(type):
        # return eval(type + "()")
        if type == "Circle": return Circle()
        if type == "Square": return Square()
        if type == "Triangulo": return Triangulo()
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")

class Square(Shape):
    def draw(self): print("Square.draw")
    def erase(self): print("Square.erase")

class Triangulo(Shape):
    def draw(self): print("Dibujar Triángulo")
    def erase(self): print("Borrar Triángulo")

# Generate shape name strings:
def shapeNameGen(n):
    types = Shape.__subclasses__()
    print(types)
    for i in range(n):
        yield random.choice(types).__name__

shapes = [Shape.factory(i) for i in shapeNameGen(7)]
print(shapes)

for shape in shapes:
    shape.draw()
    shape.erase()

# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/
# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html#simple-factory-method

input("Press ENTER to EXIT")