# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a lista lnumeros
# 2 - receber a lista lsletras
# 3 - receber a referencia r
# 4 - l_saida = []
# 5 - l_numeros = []
# 6 - N = len(lsletras)
# 7 - iterar range(N) com k
# 8 - verificar se lnumeros[k] >= r
# 8.1 - se lnumeros[k] >= r, então l_saida.append(lsletras[k]) e l_numeros.append(lnumeros[k])
# 9 - exibir l_saida, l_numeros
# --------- Fim ------------
def qt_13(lnumeros,lsletras,r):
  l_saida = []
  l_numeros = []
  N = len(lsletras)
  for k in range(N):
    if lnumeros[k] >= r:
      l_saida.append(lsletras[k])
      l_numeros.append(lnumeros[k])
  return l_saida,l_numeros
validos,n = qt_13([5, 4, 3, 11, 12, 1],["AA", "AB", "BA", "BB", "CA", "AC"],8)
print("Produtos na validade: ",validos,n)