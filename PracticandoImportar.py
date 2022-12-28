import ModuloPracticarImportar

print(ModuloPracticarImportar.greeting("Jonathan"))
print(ModuloPracticarImportar.person1["age"])
print(ModuloPracticarImportar.listita[0])
print(ModuloPracticarImportar.tuplita[0])


print("\n\n")


import ModuloPracticarImportar as MPI

print(type(MPI.greeting), MPI.greeting("Jonathan"))
print(type(MPI.person1), MPI.person1["age"])
print(type(MPI.listita), MPI.listita[0])
print(type(MPI.tuplita), MPI.tuplita[0])


print("\n\n")


import platform
x = platform.system()
print(x)


print("\n\n")


from ModuloPracticarImportar import person1, listita

# Note: When importing using the from keyword,
# do not use the module name when referring to elements in the module.
# Example: person1["age"], not ModuloPracticarImportar.person1["age"]


print(person1["age"])
print(listita[0])
# print(tuplita[0])  # NameError: name 'tuplita' is not defined


input("Press ENTER to EXIT")