def LineaTriangulo(numEspaciosDelante, numFila):
	trozoAsteriscos = "*" * int((2*numFila)-1)
	



	trozoEspacios = "x" * numEspaciosDelante
	return trozoEspacios + trozoAsteriscos


numLineasTriangulo = int(input("Introduzca el número de líneas... "))
espaciosIniciales = numLineasTriangulo-1
for contandoFilas in range(1, numLineasTriangulo+1):
	print(LineaTriangulo(espaciosIniciales, contandoFilas))
	espaciosIniciales = espaciosIniciales-1



input("Press ENTER to EXIT")