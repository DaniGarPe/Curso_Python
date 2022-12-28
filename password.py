# tamaño 6

# letrasMinusculas = 97-122

# letrasMayusculas = 65-90

# numeros 0 48-57

# caracteres = 35,38,64

# chr(random.randint(48,57))

import random

longitud = int(input("Introduzca el tamaño de la contraseña: "))

if longitud < 8 :
	print("La contraseña es muy pequeña, es recomendable que sea mayor a 8 caracteres.")

contador = 0

password = ""

while(contador != longitud):

	opcion = random.randint(1,4)

	if opcion == 1:
	    # Letras minusculas
		password += chr(random.randint(97,122))
	elif opcion == 2:
	    # Letras mayusculas
		password += chr(random.randint(65,90))
	elif opcion == 3:
	    # Numeros
		password += chr(random.randint(48,57))
	elif opcion == 4:
        # Caraceteres
		caracter = random.randint(1,3)

		if caracter == 1:
			password += chr(35)
		elif caracter == 2:
			password += chr(38)
		elif caracter == 3:
			password += chr(64)

	contador += 1

print("Su contraseña es: " , password)