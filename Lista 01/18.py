# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a listas l1,l2
# 2 - d = 0
# 3 - N = len(l1)
# 4 - iterar range(N) com k
# 5 - verificar se l1[k] != l2[k]
# 5.1 - se se l1[k] != l2[k], então d = d + 1
# 6 - exibir d
# --------- Fim ------------
def qt_18(l1,l2):
    d = 0
    N = len(l1)
    for k in range(N):
        if l1[k] != l2[k]:
            d = d + 1
    return d
distancia = qt_18([1, 0, 0, 1, 1, 0, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1])
print("A distância de Hamming entre as sequências é:",distancia)