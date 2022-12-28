def calcular_Pedriscos(p_num):
        
    if (p_num % 2 == 0):
        p_num = p_num/2
    else:
        p_num = 3 * p_num + 1
        
    print(p_num)
    
    if p_num != 1:
        calcular_Pedriscos(p_num)

# fin funcion

num = int(input("Introduzca un numero: "))

calcular_Pedriscos(num)