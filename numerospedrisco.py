# Numeros pedriscos

num = int(input("Introduzca un numero: "))

contador = 0

while(num > 1):

	if num%2 == 0:
		num = num/2
		print(num)
		contador += 1
	else:
		num = 3 * num + 1
		print(num)
		contador += 1
		
print("Ha necesitado :" , contador, " iteraciones")

input("Pulsa para salir")