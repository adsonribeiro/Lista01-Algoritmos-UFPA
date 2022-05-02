# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a lista lnomes
# 2 - receber a lista lidades
# 3 - receber i
# 4 - receber f
# 5 - l_saida = []
# 6 - N = len(lnomes)
# 7 - iterar range(N) com k
# 8 - verificar se lidadek[k] >=  i e lidades[k] <= f
# 8.1 - se se lidadek[k] >=  i e lidades[k] <= f, então l_saida.append(lnomes[k])
# 9 - exibir l_saida
# --------- Fim ------------
def qt_14(lnomes,lidades,i,f):
  l_Saida = []
  N = len(lnomes)
  for k in range(N):
    if  lidades[k] >= i and lidades[k] <= f:
      l_Saida.append(lnomes[k])
  return l_Saida
pcampanha = qt_14(["Ramon", "Arnaldo", "Raquel", "Pedro", "Rafael"],[23, 45, 27, 60, 45],20,30)
print("participarão da campanha:", pcampanha)