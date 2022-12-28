# El área de un círculo es pi multiplicado por el radio al cuadrado (A = π r²).
import math


def AreaCirculo(radio):
    return math.pi * radio * radio

radio = int(input("Introduzca radio..."))
print("El área del círculo de radio ", radio, " es igual a", AreaCirculo(radio))


# La longitud de una circunferencia es igual a 2 pi por el radio
def LongitudCircunferencia(radio):
    return math.pi * 2 * radio

radio = int(input("Introduzca radio..."))
print("La longitud de la circunferencia de radio ", radio, " es igual a", LongitudCircunferencia(radio))

input("Press ENTER to EXIT")