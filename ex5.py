def countCaracter(frase, ignore:bool = False):
  if ignore == True:
    return len(frase.replace(" ", ""))
  else:
    return len(frase)
  
print(countCaracter("Eu amocarne com batatas",True))