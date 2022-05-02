# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a lista ls
# 2 - igualar qtd_ms,qtd_mi,,qtd_qs,qtd_i = 0
# 3 - iterar ls com x
# 4 - verificar se x == 0
# 4.1 - se x == 0 , então qtd_ms = qtd_ms + 1
# 5 - verificar se x > 5
# 5.1 - se x > 5 , então qtd_mi = qtd_mi + 1
# 6 - verificar se x >= 1 e x <=3
# 6.1 - se x >=1 e x <=3, então qtd_qs = qtd_qs + 1
# 7 - verificar se x >= 4 e x <= 5
# 7.1 - se x >= 4 e x <= 5 , então qtd_i = qtd_i + 1
# 8 - exibir qtd_ms,qtd_mi,qtd_qs,qtd_i
# --------- Fim ------------
def qt_09(ls):
    qtd_ms = 0
    qtd_qs = 0
    qtd_i = 0
    qtd_mi = 0
    for x in ls:
        # muito seguro
        if x == 0:
            qtd_ms = qtd_ms + 1
        # muito inseguro
        if x > 5:
            qtd_mi = qtd_mi + 1
        #quase seguro
        if (x >= 1 and x <= 3):
            qtd_qs = qtd_qs + 1
        #inseguro
        if (x >= 4 and x <= 5):
            qtd_i = qtd_i + 1
    
    return qtd_ms,qtd_mi,qtd_qs,qtd_i
muito_seguro, muito_inseguro, quase_seguro, inseguro = qt_09([1, 3, 4, 5, 6, 7, 8, 9])
print("Muito seguro:",muito_seguro,"| Muito inseguro:",muito_inseguro,"| Quase Seguro:",quase_seguro,"|Inseguro:",inseguro)
    
