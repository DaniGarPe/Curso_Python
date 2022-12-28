class Triangulo:
    atributoDeClaseQueEnEsteEjemploNoSirveParaNada = 5

    # Initializer / Instance Attributes
    def __init__(self, b, a):
        self.base = b
        self.altura = a

    # método de instancia calcularArea que nos proporciona el área del triángulo dada su base y su altura
    def calcularArea(self):
        self.otrodato = 7
        return "El triángulo de base {} y altura {} tiene un área de {}".format(self.base, self.altura, self.base*self.altura/2)

# instantiate the object
triangulo1 = Triangulo(5, 3)
triangulo2 = Triangulo(50, 30)

# call our instance methods
print(triangulo1.calcularArea())
print(triangulo2.calcularArea(), "\n")
print(triangulo1.otrodato)
triangulo1.otrodato = 66
print(triangulo1.otrodato)
print(triangulo2.otrodato, "\n")
print(triangulo1.atributoDeClaseQueEnEsteEjemploNoSirveParaNada)
print(triangulo2.atributoDeClaseQueEnEsteEjemploNoSirveParaNada, "\n")

# Python objects store their instance variables in a dictionary that belongs to the object.
# vars(x) returns this dictionary (as does x.__dict__).
# dir(x), on the other hand, returns a dictionary of x's "attributes,
# its class's attributes, and recursively the attributes of its class's base classes."

print ("Info del objeto triángulo mostrando atributos ÚNICAMENTE de instancia usando vars: ", vars(triangulo1))
print ("Info del objeto triángulo mostrando atributos ÚNICAMENTE de instancia usando dict: ", triangulo1.__dict__)
print ("Info del objeto triángulo mostrando atributos de instancia y de clase: ", dir(triangulo1))

input("Press ENTER to EXIT")