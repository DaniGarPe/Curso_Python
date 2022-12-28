# Piramide de asteriscos segun el numero de lineas que introduce el usuario

lineas = int(input("Introduce el numero de filas: "))

def piramide(p_lineas):
	for numLinea in range(0, p_lineas, 1):
		espacios = p_lineas - numLinea - 1
		asteriscos = numLinea * 2 + 1
		print(" " * espacios , end="")
		print("*" * asteriscos)

piramide(lineas)