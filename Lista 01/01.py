# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a lista ls
# 2 - qtd = 0
# 3 - iterar com x a lista ls
# 4 - verificar se x < 7
# 4.1 - se x < 7, então qtd = qtd + 1
# 5 - exibir qtd
# --------- Fim ------------
def qt_01 (ls):
    qtd = 0
    for x in ls:
        if x < 7:
            qtd = qtd + 1
    return qtd
fora = qt_01([7,6,5,4,3,6,7,8,20,3,12])
print("Embalagens fora do padrão: ",fora)