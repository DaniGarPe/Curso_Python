#Calculadora

#1-multiplicar
#2-dividir
#3-sumar
#4-restar
#5-salir

#selecciona una opcion

#introduce primer numero
#introduce segundo numero

#el resultado es

#desea continuar ???

###############################

import os

def calcular(p_opcion):
    if(p_opcion == 1):
        print("El resultado de la multiplicacion es: {}".format(multiplicar()))
    elif(p_opcion == 2):
        print("El resultado de la division es: {}".format(suma()))
    elif(p_opcion == 3):
        print("El resultado de la suma es: {}".format(dividir()))
    elif(p_opcion == 4):
        print("El resultado de la resta es: {}".format(restar()))

# Fin calcular

def suma():
    num1 = int(input("introduce primer numero: "))
    num2 = int(input("introduce segundo numero: "))
    return num1 + num2

# Fin suma

def multiplicar():
    num1 = int(input("introduce primer numero: "))
    num2 = int(input("introduce segundo numero: "))
    return num1 * num2

# Fin multiplicar

def dividir():
    num1 = int(input("introduce primer numero: "))
    num2 = int(input("introduce segundo numero: "))
    return num1 / num2

# Fin dividir

def restar():
    num1 = int(input("introduce primer numero: "))
    num2 = int(input("introduce segundo numero: "))
    return num1 - num2

# Fin restar

def menu():
    print("Calculadora")
    print("*****************")
    print()
    print("1- multiplicar")
    print("2- dividir")
    print("3- sumar")
    print("4- restar")
    print("5- salir")

# Fin menu

opcion = 0

menu()
print()
opcion = int(input("Elija una opcion: "))

while(opcion != 5):

    calcular(opcion)
    print()
    continuar = input("Desea continuar ??? s/n: ")

    while( (continuar != "s") and (continuar != "n") and (continuar != "S") and (continuar != "N")):
        continuar = input("Desea continuar ??? s/n: ")
    
    if(continuar == 'n' or continuar == 'N'):
        opcion = 5
    elif(continuar == 's' or continuar == 'S'):
        os.system('cls')
        menu()
        print()
        opcion = int(input("Elija una opcion: "))
    else:
        print("Opcion no valida")

input("Pulsa cualquier tecla para salir")