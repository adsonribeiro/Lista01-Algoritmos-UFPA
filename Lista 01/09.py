def qt_09(ls):
    qtd_ms = 0
    qtd_s = 0
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
    
    return qtd_ms,qtd_qs,qtd_i
muito_seguro, quase_seguro, inseguro = qt_09([1, 3, 4, 5, 6, 7, 8, 9])
print("Muito Seguro = ",muito_seguro,"| quase seguro = ",quase_seguro,"| Inseguro = ",inseguro)
    
