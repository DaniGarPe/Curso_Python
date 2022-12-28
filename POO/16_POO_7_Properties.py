#--------------------------
class P(object):

    def __init__(self, value):
        self.x = value  # Will call the setter. Note just x here
        # self.__x = value  # Will not call the setter
    @property
    def x(self):
        print("Getting value")
        return self.__x

    @x.setter
    def x(self, value):
        print("Setting value")
        if value < 0:
            self.__x = 0
        elif value > 1000:
            self.__x = 1000
        else:
            self.__x = value


p1 = P(1001)
print (p1.x)
p1.x = -12
print (p1.x)

input("Press ENTER to EXIT")
# https://www.python-course.eu/python3_properties.php
# https://stackoverflow.com/questions/598077/why-does-foo-setter-in-python-not-work-for-me
# https://www.programiz.com/python-programming/property


# You seem to be using classic old-style classes in python 2.
# In order for properties to work correctly you need to use new-style classes instead
# (in python 2 you must inherit from object). Just declare your class as MyClass(object)...

# Applications:
# By using property() method, we can modify our class and implement the value constraint without any change required to the client code.
# So that the implementation is backward compatible.