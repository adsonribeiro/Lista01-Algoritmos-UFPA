def qt_11(r,ls):
  qtd = []
  for x in ls:
    if x >= r:
      qtd.append(x)
  return qtd
produtos = qt_11(8,[5, 4, 3, 11, 1, 1, 8 ,10, 11, 3, 4, 2, 10])
print("Produtos na validade = ", produtos)