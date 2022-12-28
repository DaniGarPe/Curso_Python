# sumar las cifras de un numero
# 34567
# 3+4+5+6+7



resultado = 0

num = input("Introce un numero entero: ")

for i in num:
    resultado += int(i)
    
print("La suma de los digitos es: {}".format(resultado))