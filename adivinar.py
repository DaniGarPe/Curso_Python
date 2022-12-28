import random

numPC = random.randint(1,100)
#print(numPC)
numUser = 0

contador = 0

while(numPC != numUser):
    
    numUser = int(input("Introduzca un numero del 1 al 100: "))

    if(numUser > numPC ):
        print("El numero buscado es menor que " , numUser)

    elif(numUser < numPC ):
        print("El numero buscado es mayor que " , numUser)

    contador += 1

print("Enhorabuena !!! Has acertado, el numero era ", numPC , " has necesitado ", contador , " intentos.")
print("Fin del juego. ")

input("Pulsa cualquier boton para salir. ADIOS")