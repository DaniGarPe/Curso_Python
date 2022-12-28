# Manera 1 sin funciones
base = input("Introduzca la base del triangulo")
print(type(base))
base = int(base)
print(type(base))

altura = int(input("Introduzca la altura del triangulo"))

area = (base*altura)/2
print("Area triángulo", area, type(area))


# Manera 2 usando funciones
def AreaTriangulo(base, altura):
    return base*altura/2


print(AreaTriangulo(int(input("base")), int(input("altura"))))


# Manera 3 usando objetos...
# miTriangulo = new Triangulo(5, 3)
# print(        miTriangulo.calcularArea()    )
input("Press ENTER to EXIT")