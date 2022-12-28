# Piramide de asteriscos hueca segun el numero de lineas que introduce el usuario

num = int(input("Introduce el numero de filas: "))

def piramideVacia(p_lineas):
	for numLinea in range(0, p_lineas, 1):
		espacios = p_lineas - numLinea - 1
		vacios = numLinea * 2 + 1

		print(" " * espacios , end="")

		if numLinea == 0:
			print("*")
		elif numLinea == p_lineas-1:
			print("*" * vacios)
		else:
			vacios = vacios - 2
			print("*" + " " * vacios + "*")

piramideVacia(num)