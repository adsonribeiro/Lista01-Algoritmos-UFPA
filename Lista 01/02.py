# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a media(media)
# 2 - rebeber a lista(ls)
# 3 - qtd = 0
# 4 - iterar com x a lista ls
# 5 - verificar se x > media
# 5.1 - se x > media, então qtd = qtd + 1
# 6 - exibir qtd
# --------- Fim ------------
def qt_02 (media,ls):
    qtd = 0
    for x in ls:
        if x > media:
            qtd = qtd + 1
    return qtd
acima = qt_02(6,[6, 6, 5, 8, 6, 5, 4, 6])
print("A quantidade de aluno acima da media foi: ", acima)