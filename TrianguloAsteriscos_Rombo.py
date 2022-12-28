numFilas = int(input("Intro num de filas"))
espaciosIniciales = numFilas
for fila in range(1, numFilas + 1):
    print("{}{}".format(" " * espaciosIniciales, "*" * (2 * fila - 1)))
    espaciosIniciales = espaciosIniciales - 1

print("\n\n\n")


espaciosIniciales = numFilas
for fila in range(1, numFilas + 1):
	if (fila==1 or fila==numFilas):
		print("{}{}".format(" " * espaciosIniciales, "*" * (2 * fila - 1)))
	else:
		print("{}{}{}{}".format(" " * espaciosIniciales, "*", " " * (2 * fila - 3), "*"))
	espaciosIniciales = espaciosIniciales - 1

print("\n\n\n")


espaciosIniciales = numFilas
for fila in range(1, numFilas + 1):
    print("{}{}".format(" " * espaciosIniciales, "*" * (2 * fila - 1)))
    espaciosIniciales = espaciosIniciales - 1


espaciosIniciales=2
for fila in range(numFilas-1, 0, -1):
    print("{}{}".format(" " * espaciosIniciales, "*" * (2 * fila - 1)))
    espaciosIniciales = espaciosIniciales + 1



print("\n\n\n")


espaciosIniciales = numFilas
for fila in range(1, numFilas + 1):
	if (fila==1 or fila==numFilas):
		print("{}{}".format(" " * espaciosIniciales, "*" * (2 * fila - 1)))
	else:
		print("{}{}{}{}".format(" " * espaciosIniciales, "*", " " * (2 * fila - 3), "*"))
	espaciosIniciales = espaciosIniciales - 1

espaciosIniciales=2
for fila in range(numFilas-1, 0, -1):
	if (fila==1 or fila==numFilas):
		print("{}{}".format(" " * espaciosIniciales, "*" * (2 * fila - 1)))
	else:
		print("{}{}{}{}".format(" " * espaciosIniciales, "*", " " * (2 * fila - 3), "*"))
	espaciosIniciales = espaciosIniciales + 1

print("\n\n\n")



input("Press ENTER to exit")