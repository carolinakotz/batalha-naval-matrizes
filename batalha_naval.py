def gera_matriz():
    linha = []
    for i in range(10):
        coluna = []
        for j in range(10):
            coluna.append("")
        linha.append(coluna)
    return linha




def mostra_mapa():
    cont = 0
    for i in range(cont,11):
        print("_"*21)
        if cont <11:
            print("| "*11)
    print("_"*21)


mostra_mapa()