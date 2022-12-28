def VerificarSiCentroNumerico(p_candidato):
  sumaIzq = 0
  ListaNumerosIzq=[]
  ListaNumerosDrcha=[]
  sumaLateral=0

  for numerosIzq in range(1, p_candidato):
    ListaNumerosIzq.append(numerosIzq)
    sumaIzq = sumaIzq + numerosIzq

  sumaLateral=sumaIzq

  numeroDerecha = p_candidato + 1

  while sumaIzq > 0:
    ListaNumerosDrcha.append(numeroDerecha)
    sumaIzq = sumaIzq - numeroDerecha
    numeroDerecha = numeroDerecha + 1

  if sumaIzq == 0:
    return [
      " + ".join(str(numeros) for numeros in ListaNumerosIzq) + " = " + str(sumaLateral),
      " + ".join(str(numeros) for numeros in ListaNumerosDrcha) + " = " + str(sumaLateral)
    ]   
  else:
    return None

cuantosCentrosNumericos = 3
candidato = 2

while cuantosCentrosNumericos > 0:
  info=VerificarSiCentroNumerico(candidato)
  if info != None:
    cuantosCentrosNumericos = cuantosCentrosNumericos - 1
    print(candidato)
    print(info[0])
    print(info[1])
    print("\n")

  candidato = candidato + 1

input("Press ENTER to EXIT")