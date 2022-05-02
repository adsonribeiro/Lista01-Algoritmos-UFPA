# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a sequencia alvo f
# 2 - receber a lista ls
# 3 - qtd = 0
# 4 - iterar ls com x
# 5 - verificar se x == f
# 5.1 - se x == f, então qtd = qtd + 1
# 6 - exibir qtd
# --------- Fim ------------
def qt_05(f,ls):
    qtd = 0
    for x in ls:
        if x == f:
            qtd = qtd + 1
    return qtd
sequencia = qt_05("GAGC",["TACG", "GAGC", "ATUC", "TAGC", "GAGC"])
print("a frequencia da sequencia alvo é:", sequencia)