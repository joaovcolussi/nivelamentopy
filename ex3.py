def saudacao(nome, periodo ="dia"):
  if periodo == "dia":
    return "Bom dia, aproveite essa bela manhã! " + nome
  elif periodo == "tarde":
    return "Boa tarde, aproveite essa bela tarde! " + nome
  elif periodo =="noite":
    return "Boa noite, aproveite essa bela noite! " + nome
  else:
    return "Tenha um ótimo dia!"

print(saudacao("João"))  