import os
import subprocess

def limpa_terminal():
    if os.name == "nt":
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
    print("    1   2   3   4   5   6   7   8   9  10")

    for i in range(len(matriz)):
        print("  " + "----" * len(matriz) + "-")
        print(f"{i + 1:2}|", end="")

        for j in range(len(matriz[i])):
            print(f" {matriz[i][j]:1} |", end="")

        print()

    print("  " + "----" * len(matriz) + "-")

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
    navio_lista = navios.get(navio) 
    direcao = escolhe_direcao()
    if verifica_posicao_invalida(matriz,linha,coluna,navio_lista, direcao):
        match direcao.lower():
            case "v":                              
                for i in range(len(navio_lista)):
                    matriz[linha+i][coluna] = navio_lista[i]
            case "h":
                for i in range(len(navio_lista)):
                    matriz[linha][coluna+i] = navio_lista[i]
        return True
    else:
        return False

def escolhe_direcao():
    while True:
        direcao = input(
            "Qual a direção do navio?\n"
            "[H] - Horizontal\n"
            "[V] - Vertical\n"
        ).lower()

        if direcao == "h" or direcao == "v":
            return direcao

        print("Direção inválida! Digite H ou V.")

def verifica_posicao_invalida(matriz, linha, coluna, navio, direcao):
    for i in range(len(navio)):
        if matriz[linha][coluna] == "O":
            input("Essa posição já está ocupada! Digite outra posição.\t[ENTER para continuar]")
            return False
        elif matriz[linha][coluna+1] == "O" or matriz[linha][coluna-1] == "O":
            input("Posição inválida!\t[ENTER para continuar] ")
            return False  
        elif matriz[linha-1][coluna] == "O" or matriz[linha+1][coluna]:
            input("Posição inválida!\t[ENTER para continuar] ")
            return False 
        elif matriz[linha-1][coluna+1] == "O" or matriz[linha-1][coluna-1] == "O":
            input("Posição inválida!\t[ENTER para continuar] ")
            return False
        elif matriz[linha+1][coluna+1] == "O" or matriz[linha+1][coluna-1] == "O":
            input("Posição inválida!\t[ENTER para continuar] ")
            return False
        
        if direcao == "h":
            coluna += 1
        else: 
            linha += 1
    return True
        
            
matriz = gera_matriz()
navios = cria_navios()
try:
    while(True):
        limpa_terminal()
        mostra_mapa(matriz)
        mostra_navios(navios)
        navio = escolhe_navio()
        if navio == None: 
            continue
        if navio == "0":
            break
        while True:
            i = escolhe_posicao_linha()
            j = escolhe_posicao_coluna()
            if not insere_navio(matriz,navios,i-1,j-1,navio):
                limpa_terminal()
                mostra_mapa(matriz)
                continue
            trocar_
            break
except Exception as e:
    print(e)

# print(len(navios.get("Submarino")))
# lista = navios.get("Submarino")
# lista.__delattr__
