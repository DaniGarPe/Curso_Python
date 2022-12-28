# Numeros pedriscos de 1 a 30

contador = 0

for num in range(1,31):
    
    print("Numero: ", num )
    print("")
    while(num > 1):
    
    	if num%2 == 0:
    		num = num/2
    		print(num)
    		contador += 1
    	else:
    		num = 3 * num + 1
    		print(num)
    		contador += 1
    print("")        		
    print("Ha necesitado :" , contador, " iteraciones")
    print("------------------------------------------")

input("Pulsa para salir")