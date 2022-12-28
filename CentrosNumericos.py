def VerificarSiCentroNumerico(p_candidato):
  sumaIzq = 0
  for numerosIzq in range(1, p_candidato):
    sumaIzq = sumaIzq + numerosIzq  

  numeroDerecha = p_candidato + 1
 
  while sumaIzq > 0:
    sumaIzq = sumaIzq - numeroDerecha
    numeroDerecha = numeroDerecha + 1

  if sumaIzq == 0:
    return True
  else:
    return False
    
  
cuantosCentrosNumericos = 5
candidato = 2

while cuantosCentrosNumericos > 0:
  if VerificarSiCentroNumerico(candidato) == True:
    cuantosCentrosNumericos = cuantosCentrosNumericos - 1
    print(candidato)

  candidato = candidato + 1

input("Press ENTER to EXIT")