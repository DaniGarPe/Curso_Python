print("Tablas de multiplicar")
print("---------------------")
#print("Introduce un numero distinto de cero, si introduces cero saldras")

# introduce un numero por pantalla
num = int(input("Introduce un numero: "))

#Funcion que recibe un numero y muestra su tabla de multiplicar
def multiplicar(p_num):
	

    for i in range(1, 11, 1):
    
        resu = i * p_num
        print('{} por {} = {}'.format(p_num, i, resu))

# Llamar a la funcion
multiplicar(num)

# Imprimir la documentacion
print(multiplicar.__doc__)

input("Presiona ENTER para salir")