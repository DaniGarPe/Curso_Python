import math
def SolEcuacionSegundoGrado(coef_A, coef_B, coef_C):
	discrimante = (coef_B*coef_B)-(4*coef_A*coef_C)
	if discrimante < 0:
		return "No existe solución real"
	elif discrimante == 0:  # The elif keyword is pythons way of saying
		# "if the previous conditions were not true, then try this condition".
		return -coef_B/(2*coef_A)
	else: # discrimante > 0: # The else keyword catches anything which isn't caught by the preceding conditions.
		raiz = math.sqrt(discrimante)
		soluciones = []  # Lista vacía
		soluciones.append((-coef_B+raiz)/(2*coef_A))
		soluciones.append((-coef_B-raiz)/(2*coef_A))
		return soluciones



print("Soluciones de la ec. de segundo grado con coeficientes a={}, b={} y c={}...\n\t{}\n"
.format(2, 5, 777, SolEcuacionSegundoGrado(2, 5, 777)))  # No existe solución

print("Soluciones de la ec. de segundo grado con coeficientes a={}, b={} y c={}...\n\t{}\n"
.format(1, 2, 1, SolEcuacionSegundoGrado(1, 2, 1)))  # Una solución

print("Soluciones de la ec. de segundo grado con coeficientes a={}, b={} y c={}...\n\t{}\n"
.format(2, 5, 2, SolEcuacionSegundoGrado(2, 5, 2)))  # Dos soluciones

input("Press ENTER to EXIT")