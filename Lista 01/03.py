def qt_03 (ls):
    mal = ls [0]
    for x in ls:
        if x > mal:
            mal = x
    return mal
print(qt_03([1.7, 1.88, 1.5, 1.32, 1.68, 1.59]))