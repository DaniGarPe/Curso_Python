import math


def check_Si_Primo(p_candidato):
    for divisorFastidiador in range(2, int(math.sqrt(p_candidato))+1):
        if (p_candidato % divisorFastidiador == 0):
            return False
    return True

for candidato in range(2, 101):
    if (check_Si_Primo(candidato) is True):
        print(candidato, end=" - ")

print("\n")

cuantosPrimos = 100
candidato = 2
contador_primos_por_fila = 0
while(cuantosPrimos > 0):
    if (check_Si_Primo(candidato) is True):
        contador_primos_por_fila += 1
        print(candidato, end=" - " if(contador_primos_por_fila < 10) else "\n")
        if(contador_primos_por_fila == 10):
            contador_primos_por_fila = 0
        cuantosPrimos -= 1
    else:
        pass
    candidato += 1


input("Press Enter to EXIT")