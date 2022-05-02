# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a lista ls
# 2 - pa = "Sim"
# 3 - r = ls[1] - ls[0]
# 4 - N = len(ls)
# 5 - iterar range(1,N) com k
# 6 - verificar se ls[k] - ls[k-1] != r
# 6.1 - se ls[k] - ls[k-1] != r, então pa = "Não"
# 7 - exibir pa
# --------- Fim ------------
def qt_17(ls):
    pa = "Sim"
    r = ls[1] - ls[0]
    N = len(ls)
    for k in range(1,N):
        if ls[k] - ls[k-1] != r:
            pa = "Não"
    return pa
spa = qt_17([1, 5, 9, 13, 17, 21, 25])
print("É PA: ",spa)