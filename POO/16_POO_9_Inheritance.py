# Python Object Inheritance
# Inheritance is the process by which one class takes on
# the attributes and methods of another.
# Newly formed classes are called child classes,
# and the classes that child classes are derived from are called parent classes.

# It’s important to note that child classes override or extend the functionality
# (e.g., attributes and behaviors) of parent classes.
# In other words, child classes inherit all of the parent’s attributes and behaviors
# but can also specify different behavior to follow.
# The most basic type of class is an object,
# which generally all other classes inherit as their parent.

# When you define a new class,
# Python 3 it implicitly uses object as the parent class.
# So the following two definitions are equivalent:

# class Dog(object):
#     pass

# # In Python 3, this is the same as:

# class Dog:
#     pass


# Dog Park Example
class Dog:
    def __init__(self, breed):
        self.breed = breed
spencer = Dog("German Shepard")
print(spencer.breed)
# 'German Shepard'
sara = Dog("Boston Terrier")
print(sara.breed)
# 'Boston Terrier'
print("\n")




# Extending the Functionality of a Parent Class
# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)
print(jim.description())

# Child classes have specific attributes
# and behaviors as well
print(jim.run("slowly"))
print("\n")

# Parent vs. Child Classes
# The isinstance() function is used to determine
# if an instance is also an instance of a certain parent class.

# Is jim an instance of Dog()?
print(isinstance(jim, Dog))

# Is julie an instance of Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

# Is johnny walker an instance of Bulldog()
johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))
print("\n")

# Is julie and instance of jim?
# ERROR TypeError: isinstance() arg 2 must be a class, type, or tuple of classes and types
# print(isinstance(julie, jim))  

# Make sense? Both jim and julie are instances of the Dog() class,
# while johnnywalker is not an instance of the Bulldog() class.
# Then as a sanity check, we tested if julie is an instance of jim,
# which is impossible since jim is an instance of a class 
# rather than a class itself—hence the reason for the TypeError.


# Overriding the Functionality of a Parent Class
# Remember that child classes can also override
# attributes and behaviors from the parent class. For examples:
class Dog:
    species = 'mammal'

class SomeBreed(Dog):
    pass

class SomeOtherBreed(Dog):
    species = 'reptile'

frank = SomeBreed()
print(frank.species)
# 'mammal'

beans = SomeOtherBreed()
print(beans.species)
# 'reptile'

# The SomeBreed() class inherits the species from the parent class,
# while the SomeOtherBreed() class overrides the species, setting it to reptile.


print("\n")
print(beans.__class__.__bases__[0].species)
# 'mammal'
clasePadre = super(beans.__class__, beans)
# Remember that, to use super() in two argument form,
# it is necessary that the object passed as the second argument
# is an instance of the type passed as first argument.
print(clasePadre.species)
# 'mammal'
print(beans.__class__.__bases__[0].species == super(beans.__class__, beans).species)
# True

# https://stackoverflow.com/questions/2265060/python-how-to-access-parent-class-object-through-derived-class-instance

input("Press ENTER to EXIT")