class Dog:
	# pass we used the Python keyword pass here.
	# This is very often used as a place holder where code will eventually go.
	# It allows us to run this code without throwing an error.

	# Class Attribute
    species = 'mammal'

	# Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes
print("{} is {} and {} is {}.".format(philo.name, philo.age, mikey.name, mikey.age))

# Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))

# Dos maneras de acceder al atributo (propiedad) de clase desde una instancia
print(philo.species == philo.__class__.species)

print(philo.name, philo.age, philo.species)
print(mikey.name, mikey.age, mikey.species)

# call our instance methods
print(mikey.description())
print(mikey.speak("Gruff Gruff"))

input("Press ENTER to EXIT")