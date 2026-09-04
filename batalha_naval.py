import os

def gera_matriz():
    linha = []
    for i in range(10):
        coluna = []
        for j in range(10):
            coluna.append("")
        linha.append(coluna)
    return linha


def mostra_mapa(matriz):
    for i in range(10):
        for j in range(10):
            print(f"{matriz[i][j]}|", end="\n" if j==10 else"")




mapa = gera_matriz()

mapa[0][0] = "O"
mostra_mapa(mapa)