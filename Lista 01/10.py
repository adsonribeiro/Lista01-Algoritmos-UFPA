# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a lista ls
# 2 - qtd = []
# 3 - iterar ls com x
# 4 - verificar se x == "R" ou x == "r"
# 4.1 - se x == "R" ou x == "r", então qtd.append(x)
# 5 - exibir qtd
# --------- Fim ------------
def qt_10(ls):
    qtd = []
    for x in ls:
        if x[0] == "R" or x[0] == "r":
            qtd.append(x)
    return qtd
comeca_r = qt_10(["Ramon", "Arnaldo", "Raquel", "Pedro", "Rafael"])
print("Nomes que começam com R:",comeca_r)