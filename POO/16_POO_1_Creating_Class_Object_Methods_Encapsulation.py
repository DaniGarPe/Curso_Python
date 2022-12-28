# Example 1: Creating Class and Object in Python

class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, param_name, param_age):
        self.name = param_name
        self.age = param_age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old\n".format(woo.name, woo.age))

# Example 2 : Creating Methods in Python
class Parrot:
    
    # instance attributes
    def __init__(self, param_name, param_age):
        self.name = param_name
        self.age = param_age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
print("\n")

# Example 4: Data Encapsulation in Python
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 121  # error no se puede asignar valor a una propiedad "privada"
# (no existen pero bueno) de esta manera, hemos creado otra propiedad
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

print(c.__maxprice)  # Imprimimos el valor de la propiedad creada por error.

otroPC=Computer()
# print(otroPC.__maxprice)  # Menos mal que el otro objeto no la tiene y esta línea da un error


input("Press ENTER to EXIT")
# https://www.programiz.com/python-programming/object-oriented-programming