# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a velocidade r
# 2 - receber a lista ls
# 3 - qtd = 0 e soma = 0
# 4 - iterar ls com x
# 5 - soma = soma + x
# 6 - verificar se soma <= r
# 6.1 - se soma <= r , então qtd = qtd + 1
# 7 - exibir qtd
# --------- Fim ------------
def qt_06 (r,ls):
    qtd = 0
    soma = 0
    for x in ls:
        soma = soma + x
        if soma <= r:
            qtd = qtd + 1
    return qtd
item = qt_06(20,[2, 3, 4, 7, 1, 2, 30, 13, 25, 1, 3])
print("a quatidade de itens que podem ser somados são:",item)