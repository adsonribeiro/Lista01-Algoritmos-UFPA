# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a lista ls
# 2 - qtd = 0 e c = 0
# 3 - iterar ls com x
# 4 - c = c + 1
# 5 - verificar se x == c
# 5.1 - se x == c , então qtd = qtd + 1
# 6 - exibir qtd
# --------- Fim ------------
def qt_07(ls):
    qtd = 0
    c = 0
    for x in ls:
        c = c + 1
        if x == c:
            qtd = qtd + 1
    return qtd
recebe = qt_07([1, 2, 4, 8, 6, 3, 7])
print("a quantidade de candidatos que ganharão o brinde é:",recebe)