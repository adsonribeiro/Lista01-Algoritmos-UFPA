# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a lista ls
# 2 - qtd = 0, soma = 0
# 3 - iterar ls com x
# 4 - verificar se x mod 2 == 0
# 4.1 - se x mod 2 == 0, então soma = soma + x e qtd = qtd + 1
# 5 - media = soma / qtd
# 6 - exibir media
# --------- Fim ------------
def qt_04 (ls):
    qtd = 0
    soma = 0
    for x in ls:
        if x % 2 == 0:
            soma = soma + x
            qtd = qtd + 1
    media = soma / qtd
    return media
m = qt_04([2, 4, 8, 6])
print("a media dos numero pares é:",m)