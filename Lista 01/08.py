# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a lista ls
# 2 - igualar qtd_E, qtd_B, qtd_R, qtd_I = 0
# 3 - iterar ls com x
# 4 - verificar se x == "E"
# 4.1 - se x == "E" , então qtd_E = qtd_E + 1
# 5 - verificar se x == "B"
# 5.1 - se x == "B" , então qtd_B = qtd_B + 1
# 6 - verificar se x == "R"
# 6.1 - se x == "R" , então qtd_R = qtd_R + 1
# 7 - verificar se x == "I"
# 7.1 - se x == "I" , então qtd_I = qtd_I + 1
# 8 - exibir qtd_E, qtd_B, qtd_R, qtd_I
# --------- Fim ------------
def qt_08(ls):
    qtd_E = 0
    qtd_B = 0
    qtd_R = 0
    qtd_I = 0
    for x in ls:
        if x == "E":
            qtd_E= qtd_E + 1
        if x == "B":
            qtd_B = qtd_B + 1
        if x == "R":
            qtd_R = qtd_R + 1
        if x == "I":
            qtd_I = qtd_I + 1
    return qtd_E, qtd_B, qtd_R,qtd_I
E, B, R, I = qt_08(["E", "E", "B", "B", "R", "E", "B", "R", "I", "I", "R", "R", "I"])
print("E = ",E, "|B = ",B,"|R = ",R,"|I = ", I)