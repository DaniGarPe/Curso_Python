# Python Modules
# What is a Module?
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.
# Create a Module
# To create a module just save the code you want in a file with the file extension .py:

# Example
# Save this code in a file named mymodule.py

# def greeting(name):
#   print("Hello, " + name)

def DameDireccionMemoria(nombreVariable, variable):
	return ("Dirección de memoria de " + nombreVariable + " es " + str(id(variable)))

# CPython implementation detail: This is the address of the object in memory.

# Use a Module
# Now we can use the module we just created, by using the import statement:

# Example
# Import the module named mymodule, and call the greeting function:

# import mymodule   no escribir la extensión .py

# mymodule.greeting("Jonathan")

# Note: When using a function from a module, use the syntax: module_name.function_name.