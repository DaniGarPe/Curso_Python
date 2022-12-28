def factorial_iterativo(p_numero):
	resultado = 1
	for numero in range(p_numero, 1, -1):
		resultado=resultado*numero

	return resultado


def factorial_recursivo(p_numero):
	if (p_numero>1):
		return p_numero * factorial_recursivo(p_numero-1)

	if p_numero==1:
		return 1


factorial_del_numero=5


print("El factorial usando factorial_iterativo de {0} es igual a {1}"
	.format(factorial_del_numero, factorial_iterativo(5)))

print("El factorial usando factorial_recursivo de {0} es igual a {1}"
	.format(factorial_del_numero, factorial_recursivo(5)))


input("Press ENTER to EXIT")
