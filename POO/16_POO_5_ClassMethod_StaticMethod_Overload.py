"""
Instance methods need a class instance and can access the instance through self.

class method vs static method in Python

Class Method
A class method receives the class as implicit first argument, just like an instance method receives the instance.
A class method is a method which is bound to the class and not the object of the class.
They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
It can modify a class state that would apply across all the instances of the class.
For example it can modify a class variable that will be applicable to all the instances.

Static Method
A static method does not receive an implicit first argument.
A static method is also a method which is bound to the class and not the object of the class.
A static method can’t access or modify class state.
It is present in a class because it makes sense for the method to be present in class.
Static methods don’t have access to cls or self.
They work like regular functions but belong to the class’s namespace.

Class method vs Static Method
A class method takes cls as first parameter while a static method needs no specific parameters.
A class method can access or modify class state while a static method can’t access or modify it.
In general, static methods know nothing about class state.
They are utility type methods that take some parameters and work upon those parameters.
On the other hand class methods must have class as parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.

When to use what?
We generally use class method to create factory methods.
Factory methods return class object ( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions.

How to define a class method and a static method?
To define a class method in python, we use @classmethod decorator and to define a static method we use @staticmethod decorator.
Let us look at an example to understand the difference between both of them.
Let us say we want to create a class Person.
Now, python doesn’t support method overloading like C++ or Java so we use class methods to create factory methods.
In the below example we use a class method to create a person object from birth year.
As explained above we use static methods to create utility functions.
In the below example we use a static method to check if a person is adult or not.
"""

# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('Pepito', 21)
person2 = Person.fromBirthYear('Juanito', 1996)

print ("{} tiene {} años".format(person1.name, person1.age))
print ("{} tiene {} años".format(person2.name, person2.age))

# print the result
print (Person.isAdult(person1.age))

"""
Please note that naming these parameters self and cls is just a convention.
You could just as easily name them the_object and the_class and get the same result.
All that matters is that they’re positioned first in the parameter list for the method.
"""
print("\n")

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'
        
print(Pizza(['cheese', 'tomatoes']))
print(Pizza(['mozzarella', 'tomatoes']))
print(Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms']))
print(Pizza(['mozzarella'] * 4))

# The Italians figured out their pizza taxonomy centuries ago,
# and so these delicious types of pizzas all have their own names.
# We’d do well to take advantage of that and give the users
# of our Pizza class a better interface for creating
# the pizza objects they crave.

# A nice and clean way to do that is by using class methods
# as factory functions for the different kinds of pizzas we can create:

print("\n")

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

# Note how I’m using the cls argument in the margherita and prosciutto
# factory methods instead of calling the Pizza constructor directly.

# This is a trick you can use to follow 
# the Don’t Repeat Yourself (DRY) principle.
# If we decide to rename this class at some point
# we won’t have to remember updating the constructor name
# in all of the classmethod factory functions.

# Now, what can we do with these factory methods? Let’s try them out:
print(Pizza.margherita())
# Pizza(['mozzarella', 'tomatoes'])

print(Pizza.prosciutto())
# Pizza(['mozzarella', 'tomatoes', 'ham'])

# As you can see, we can use the factory functions to create new Pizza objects
# that are configured the way we want them.
# They all use the same __init__ constructor internally
# and simply provide a shortcut for remembering all of the various ingredients.

# Another way to look at this use of class methods is that
# they allow you to define alternative constructors for your classes.

# Python only allows one __init__ method per class.
# Using class methods it’s possible to add 
# as many alternative constructors as necessary.
# This can make the interface for your classes
# self-documenting (to a certain degree) and simplify their usage.

print("\n")

# Otra alternativa para la carencia de sobrecarga de constructor...
class Hello:
# def __init__(self): pass # No puedo tener varios __init__
# def __init__(self, name='max'): pass
    def __init__(self, *args, **kwargs):
        print("Creando...")
        if args:
            print(args)
        if kwargs:
            print(kwargs)


hello1 = Hello()
hello2 = Hello('Pedro')
hello3 = Hello('Pedro', 'Luis', 'Ana')
hello4 = Hello('Pedro', 'Luis', 'Ana', nombre='Zacarías', apellidos='Martín', edad='12')



# Info
# https://realpython.com/instance-class-and-static-methods-demystified/
# https://www.geeksforgeeks.org/class-method-vs-static-method-python/
# https://www.programiz.com/python-programming/methods/built-in/classmethod

input("Press ENTER to EXIT")