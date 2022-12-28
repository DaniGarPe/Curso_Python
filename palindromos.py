def reemplazos(p_cadena):
    p_cadena = p_cadena.lower()
    p_cadena = p_cadena.replace(" ", "")
    p_cadena = p_cadena.replace(",", "")
    p_cadena = p_cadena.replace("á", "a")
    p_cadena = p_cadena.replace("é", "e")
    p_cadena = p_cadena.replace("í", "i")
    p_cadena = p_cadena.replace("ó", "o")
    p_cadena = p_cadena.replace("ú", "u")
    p_cadena = p_cadena.replace("¿", "")
    p_cadena = p_cadena.replace("?", "")
    return p_cadena
    
def Palindromo(p_cadena):
    
    miCadena = limpiar(p_cadena)
    
    miCadena = miCadena.lower()
    
    if (miCadena == ''.join(reversed(miCadena))):
        resu = "Si"
    else:
        resu = "No"
    return resu
    
def limpiar(p_cadena):
    resu = ""
    p_cadena = p_cadena.lower()
    for i in p_cadena:
        if(i == " " or i == "," or i == "." or i == "¿" or i == "?"):
            resu = resu + ""
        elif(i == "á" or i == "Á"):
            resu = resu + "a"
        elif(i == "é" or i == "É"):
            resu = resu + "e"
        elif(i == "í" or i == "Í"):
            resu = resu + "i"
        elif(i == "ó" or i == "Ó"):
            resu = resu + "o"
        elif(i == "ú" or i == "Ú"):
            resu = resu + "u"
        else:
            resu = resu + i
    print()
    print("La frase Limpia es: ", resu)
    
        
    return resu

'''
def limpiar(p_cadena):

    string = p_cadena.lower()

    resu = ''.join(char for char in string if char.isalnum())
    
    print()
    print("La frase Limpia es: ", resu)
        
    return resu
''' 

cadenas = ['hola peph',
           'otto',
           'dabale arroz a la zorra el abad',
           'alli ves sevilla',
           '¿Será lodo o dólares?',
           'Isaac no ronca así',
           'No subas, abusón',
           '121',
           '22',
           '1',
           'No traces en ese cartón',
           'Arriba la birra',
           'Adán no cede con Eva y Yavé no cede con nada',
           'Le avisará Sara si va él',
           'No deseo yo ese don',
           'Mi frase inventada, no es un palíndromo.']


for cadena in cadenas:
    print(f"¿{cadena} es un palíndromo? {Palindromo(cadena)}")
    #limpiar(cadena)

input("Press Enter To Exit")