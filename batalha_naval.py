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
        for linha in range(39):
            print("-", end="", )
        print()
        for j in range(9):
            print(f" {matriz[i][j]}  |", end="")
        print()

def cria_navios():
    navios = {"Submarino": ["O","O"],
              "Contratorpedeiro" : ["O","O","O"],
              "Navio-tanque": ["O","O","O","O"],
              "Porta-aviões": ["O","O","O","O","O"]
              }
    return navios;

def escolhe_navio():
    escolha = int(input("Escolha o navio que deseja posicionar: "))
    match escolha:
        case 1: return "Submarino"
        case 2: return "Contratorpedeiro"
        case 3: return "Navio-tanque"
        case 4: return "Porta-aviões"
        case _: 
            print("Não é uma escolha válida!") 
    return None  

def escolhe_posicao_linha():
    i = int(input("Digite a linha: "))
    return i

def escolhe_posicao_coluna():
    j = int(input("Digite a coluna: "))
    return j

def mostra_navios(navios):
    cont = 0
    for key, value in navios.items():
        for i in range(len(value)):
            print(f"{value[i]}", end="")
        cont+=1
        print(f"\t[{cont}] - {key}")
        print()

def insere_navio(matriz, navios, linha, coluna, escolha):
    value = navios.get(escolha)                       
    for i in range(len(value)):
        if value[i] != "":
            matriz[linha+i][coluna] = value[i]

#def posiciona_navios(matriz):

matriz = gera_matriz()
navios = cria_navios()
escolha = -1
while(escolha != 0):
    mostra_mapa(matriz)
    mostra_navios(navios)
    escolha = escolhe_navio()
    if escolha == None: 
        continue
    i = escolhe_posicao_linha()
    j = escolhe_posicao_coluna()
    insere_navio(matriz,navios,i,j,escolha)

# print(len(navios.get("Submarino")))
# lista = navios.get("Submarino")
# lista.__delattr__
