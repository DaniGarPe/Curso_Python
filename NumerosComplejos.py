import cmath

z = complex(5, 3)  # 1º param parte real 2º param parte imaginaria

print("Parte real de número complejo ", z.real)
print("Parte imaginaria de número complejo ", z.imag)
print("Numero complejo ", z)
print("Producto de complejos z*z ", z*z)
print("Suma de complejos z+z ", z+z)

zz = complex(2, 2)
print("The phase of complex number is : ", end="")
# By default python’s print() function ends with a newline.
print(zz, cmath.phase(zz))
# printing phase of a complex number using phase()


zzz = complex(1, 1)
print("The phase of complex number is : ", end="")
print(zzz, cmath.phase(zzz))


zzzz = complex(0, 1)
print("The phase of complex number is : ", end="")
print(zzzz, cmath.phase(zzzz))


zzzzz = complex(-1, 0)
print("The phase of complex number is : ", end="")
print(zzzzz, cmath.phase(zzzzz))

input("Press ENTER to EXIT")