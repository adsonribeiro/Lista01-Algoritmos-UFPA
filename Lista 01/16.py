# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a lista lnomes
# 2 - receber o prefixo pr
# 3 - l_saida = []
# 4 - N = len(lnomes)
# 5 - iterar range(N) com k
# 6 - verificar se pr está em lnomes[k]
# 6.1 - se pr está em lnomes[k], então l_saida.append(lnomes[k])
# 7 - exibir l_saida
# --------- Fim ------------
def qt_16(lnomes,pr):
    l_saida = []
    N = len(lnomes)
    for k in range(N):
        if pr in lnomes[k]:
            l_saida.append(lnomes[k])
    return l_saida
nomes = qt_16 (["Amanda", "Amaral", "Arnaldo", "Bruno"],"Ama")
print("Usuários a partir do prefixo são:",nomes)