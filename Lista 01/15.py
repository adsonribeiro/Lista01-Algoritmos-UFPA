# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a lista ls
# 2 - l_saida = []
# 3 - N = len(ls)
# 4 - c = 0
# 5 - qtd = 0
# 6 - iterar range(N) com k
# 7 - c = c + 1
# 8 - verificar se  c % 2 == 0 e ls[k] % 2 == 0
# 8.1 - se  c % 2 == 0 e ls[k] % 2 == 0, então qtd = qtd + 1, l_saida.append(ls[k])
# 9 - exibir l_saida, qtd
# --------- Fim ------------
def qt_15 (ls):
    l_saida = []
    N = len(ls)
    c = 0
    qtd  = 0
    for k in range(N):
         c = c + 1
         if c % 2 == 0 and ls[k] % 2 == 0:
            qtd = qtd + 1
            l_saida.append(ls[k])
    return l_saida, qtd
npares, n = qt_15([1, 5, 6, 7, 3, 2, 2, 1, 0, 10, 0, 8])
print("Numeros pares e quantidade de numeros pares",npares,"quantidade de numeros",n)