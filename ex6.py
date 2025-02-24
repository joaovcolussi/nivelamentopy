def calcValor(valorproduto:float, desconto:float = None):
  return valorproduto * (1 - desconto / 100)

print(calcValor(1799.99,50))