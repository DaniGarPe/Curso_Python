# Funcion que comprueba si no es primo

def check_primo(candidato):
    for num_candidato in range(2, candidato, 1):
        if(candidato % num_candidato == 0):
            return False
    return True 

# Comprubo de uno en uno si es primo

candidato = 2

resultado = []

while(candidato < 100):
    if(check_primo(candidato) == True):
        resultado.append(candidato)
        #print("si es primo" )
    candidato += 1

print("Los numeros primos de 0 hasta 100 son: " )
print(resultado)