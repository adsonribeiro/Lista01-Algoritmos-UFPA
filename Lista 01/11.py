# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a referencia r
# 2 - receber a lista ls
# 3 - qtd = []
# 4 - iterar ls com x
# 5 - verificar se x >= r
# 5.1 - se x >= r, então qtd.append(x)
# 6 - exibir qtd
# --------- Fim ------------
def qt_11(r,ls):
  qtd = []
  for x in ls:
    if x >= r:
      qtd.append(x)
  return qtd
produtos = qt_11(8,[5, 4, 3, 11, 1, 1, 8 ,10, 11, 3, 4, 2, 10])
print("Produtos na validade = ", produtos)