# ---  Pseudocodigo ---
# --------- INICIO----------
# 1 - receber a lista ls
# 2 - mal = ls[0]
# 3 - iterar ls com x
# 4 - verificar se x > mal
# 4.1 - se x > mal, então mal = x
# 5 - exibir mal
# --------- Fim ------------
def qt_03 (ls):
    mal = ls [0]
    for x in ls:
        if x > mal:
            mal = x
    return mal
altura = qt_03([1.7, 1.88, 1.5, 1.32, 1.68, 1.59])
print("a maior altura é:", altura)