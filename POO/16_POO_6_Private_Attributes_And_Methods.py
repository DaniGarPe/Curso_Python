# PRIVATE ATTRIBUTES AND METHODS
# Private
# In the context of class, private means the attributes are only available
# for the members of the class not for the outside of the class.
# https://docs.python.org/2/tutorial/classes.html#private-variables-and-class-local-references
# “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python.

# If you want to emulate private variables for some reason, you can always use the __ prefix from PEP 8.
# Python mangles the names of variables like __foo so that they're not easily visible to code outside
# the class that contains them (although you can get around it if you're determined enough,
# just like you can get around Java's protections if you work at it).

# By the same convention, the _ prefix means stay away even if you're not technically prevented from doing so.
# You don't play around with another class's variables that look like __foo or _bar.

class P:
   def __init__(self, name, alias):
      self.name = name  # public
      self.__alias = alias  # private
      self._otrodato = 5

   def who(self):
      print('name  : ', self.name)
      print('alias : ', self.__alias)

   def __foo(self):  # private method
      print('This is private method')

   def foo(self):  # public method
      print('This is public method')
      self.__foo()


x = P(name='Alex', alias='amen')
print(x.name)  # 'Alex'
print(x._otrodato)
x._otrodato = 5555
print(x._otrodato)
print("\n")

# print(x.alias)
# Traceback (most recent call last):
# File "", line 41, in 
# AttributeError: P instance has no attribute 'alias'

# print(x.__alias)
# Traceback (most recent call last):
# File "", line 46, in 
# AttributeError: P instance has no attribute '__alias'

# But here is a magic want. One underscore('_') with the class name will do magic:
print(x._P__alias)  # 'amen'
print("\n")
x.who()  # ('name  : ', 'Alex') # ('alias : ', 'amen')
print("\n")

# x.__foo()
# Traceback (most recent call last):
# File "", line 57, in 
# AttributeError: P instance has no attribute '__foo'

# The right way of accessing private method is this:
x._P__foo()  # This is private method
print("\n")
# Of course, calling private method via public will work as expected:
x.foo()
print("\n")
# This is public method
# This is private method

input("Press ENTER to EXIT")