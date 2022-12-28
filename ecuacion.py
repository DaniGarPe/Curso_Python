import math

# 2 5 2
# 2 5 20
# 2 4 2

coefA = int(input("Introduce primer coeficiente: "))
coefB = int(input("Introduce segundo coeficiente: "))
coefC = int(input("Introduce tercer coeficiente: "))

def resolverX(p_coefA, p_coefB, p_coefC):

    discriminante = (p_coefB * p_coefB) - (4 * p_coefA * p_coefC)
    
    if discriminante > 0:
        raiz = math.sqrt(discriminante)
        sol1 = -p_coefB + raiz / 2 * p_coefA
    
    return sol1
    
print(resolverX(coefA, coefB, coefC))

