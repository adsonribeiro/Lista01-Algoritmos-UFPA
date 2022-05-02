# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a lista lnomes
# 2 - receber a lista lsaldo
# 3 - l_saida = []
# 4 - N = len(lnomes)
# 5 - iterar range(N) com k
# 6 - verificar se lsaldo[k] >= 0
# 6.1 - se lsaldo[k] >= 0, então l_saida.append(lnomes[k])
# 7 - exibir l_saida
# --------- Fim ------------
def qt_12(lnomes,lsaldo):
  l_saida = []
  N = len(lnomes)
  for k in range(N):
    if lsaldo[k] >= 0:
      l_saida.append(lnomes[k])
  return l_saida
saldop = qt_12(["Ramon", "Arnaldo", "Raquel", "Pedro", "Rafael"],[100, -500, -1, 1500, 90])
print("Usuários com saldo positivo:",saldop)