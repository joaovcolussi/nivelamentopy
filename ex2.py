def calcular_media(n1:float, n2:float, n3:float, peso:bool = False):
  if peso == True:
    return (n1 * 2 + n2 * 3 + n3 * 5) / (2 + 3 + 5)
  
print(calcular_media(7,7,5,True))