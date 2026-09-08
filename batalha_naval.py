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
        for linha in range(43):
            print("-", end="", )
        print()
        for j in range(10):
            print(f" {matriz[i][j]}  |", end="")
        print()

def cria_lista_navios():
    navios = [["","","","O","O"],
              ["","","O","O","O"],
              ["","O","O","O","O"],
              ["O","O","O","O","O"]]
    return navios;

def posiciona_navios(matriz):
    navios = cria_lista_navios()
    escolha = -1
    while(escolha != 0): 
        mostra_mapa(matriz)
        print("\t(1)\t(2)\t(3)\t(4)")
        for i in range(4):
            for j in range(5):
                print(f"\t{navios[i][j]}\t", end="")
            print()
        escolha = int(input("\nEscolha o naviu que deseja posicionar: "))
        
      

    

        






        





mapa = gera_matriz()
posiciona_navios(mapa)
