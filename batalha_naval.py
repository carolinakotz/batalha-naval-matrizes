import os
import subprocess

def limpa_termianl():
    if os == "nt":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear")        
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
    navio = int(input("Escolha o navio que deseja posicionar: "))
    match navio:
        case 0: return "0"
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

def insere_navio(matriz, navios, linha, coluna, navio):
    value = navios.get(navio) 
    direcao = escolhe_direcao()
    match direcao.lower():
        case "v":                              
            for i in range(len(value)):
                matriz[(linha-1)+i][(coluna-1)] = value[i]
        case "h":
            for i in range(len(value)):
                matriz[(linha-1)][(coluna-1)+i] = value[i]

def escolhe_direcao():
    direcao = input("Qual a direção do navio\n[H] - Horizontal\n[V] - Vertical")
    return direcao

matriz = gera_matriz()
navios = cria_navios()
while(True):
    limpa_termianl()
    mostra_mapa(matriz)
    mostra_navios(navios)
    navio = escolhe_navio()
    if navio == None: 
        continue
    if navio == "0":
        break
    i = escolhe_posicao_linha()
    j = escolhe_posicao_coluna()
    insere_navio(matriz,navios,i,j,navio)

# print(len(navios.get("Submarino")))
# lista = navios.get("Submarino")
# lista.__delattr__
