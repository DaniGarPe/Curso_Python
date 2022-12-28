# Funcion que comprueba si no es primo

def check_primo(candidato):
    for num_candidato in range(2, candidato, 1):
        if(candidato % num_candidato == 0):
            return False
    return True 

# Comprubo de uno en uno si es primo

candidato = 2

resultado = []

limite = int(input("Introduce el numero de numeros primos que deseas: "))

while(len(resultado) < limite):
    if(check_primo(candidato) == True):
        resultado.append(candidato)
    candidato += 1

print("Los {} primeros numeros primos son: ".format(limite))
# ALTERNATIVA: print("Los" , limite , "primeros numeros primos son: ")

print(resultado)