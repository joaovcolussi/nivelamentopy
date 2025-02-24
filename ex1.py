def converterTemp(temperatura:float, escala:bool = "C"):
  if escala == "C":
    return (temperatura - 32) * 5/9
  elif escala == "F":
    return (temperatura * 9/5) + 32
  
print(converterTemp(32))