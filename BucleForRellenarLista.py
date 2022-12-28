import Module

marcasCoches =[]
print(Module.DameDireccionMemoria("marcasCoches", marcasCoches))
for x in range(0, 6):
    marcasCoches.append("marca " + str(x) + " " + input("Intro marca"))

print(marcasCoches)
print(Module.DameDireccionMemoria("marcasCoches", marcasCoches))

marcasCoches[0]="Cambiando primera marcaaaaaaaaaaaa"
print(marcasCoches)
print(Module.DameDireccionMemoria("marcasCoches", marcasCoches))



cadena="hola"
print(Module.DameDireccionMemoria("cadena", cadena))

# print(locals())


cadena="adios"
print(Module.DameDireccionMemoria("cadena", cadena))

cadena="hola"
print(Module.DameDireccionMemoria("cadena", cadena))
input("Press ENTER to EXIT")