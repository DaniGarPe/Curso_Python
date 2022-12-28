# 5 != 5*4 + 5*3 + 5*2 + 5*1
# n != n*(n-1) + n*(n-2) + n*(n-3) + n*(n-4)

n = int(input("Introduce un muero: "))
resu = 1

for i in range(1, n + 1):
    resu = resu * i
    
print("El factorial de ", n , " es: " , resu)