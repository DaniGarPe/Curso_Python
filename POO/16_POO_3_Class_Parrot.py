class Parrot:
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))


blu.__class__.species='tomate 1'  # OK
# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

woo.__class__.species='tomate 2'  # OK

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

Parrot.species='tomate 3'  # OK

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

print("\n\n")
print("Especie de blu {}".format(blu.species))
blu.species='lechuga'  # esto NO funciona
# We should be careful when changing value of class variable.
# If we try to change class variable using object,
# a new instance (or non-static) variable for that particular object is created
# and this variable shadows the class variables.
print("Especie de blu {}".format(blu.species))
print("\n\n")

print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

print("{} is {} years old y tiene la variable propia especie de {} y pertenece a la especie {}"
	.format( blu.name, blu.age, blu.species, blu.__class__.species))
print("{} is {} years old y tiene la especie de {}".format( woo.name, woo.age, woo.species))



# https://www.geeksforgeeks.org/g-fact-42-changing-class-members-python/

# https://www.programiz.com/python-programming/object-oriented-programming

print("\n\n")
for attr, value in blu.__dict__.items():
    print(attr, value)

print("\n\n")

for attr, value in woo.__dict__.items():
    print(attr, value)

print("\n\n")

for attr, value in Parrot.__dict__.items():
    print(attr, value)

input("Press ENTER to EXIT")