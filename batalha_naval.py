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
    return navios

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
    tamanho = len(navio)

    if linha < 0 or linha >= len(matriz):
        input("Linha inválida! [ENTER para continuar]")
        return False

    if coluna < 0 or coluna >= len(matriz[0]):
        input("Coluna inválida! [ENTER para continuar]")
        return False

    if direcao == "h" and coluna + tamanho > len(matriz[0]):
        input("O navio não cabe nessa posição! [ENTER para continuar]")
        return False

    if direcao == "v" and linha + tamanho > len(matriz):
        input("O navio não cabe nessa posição! [ENTER para continuar]")
        return False

    for i in range(tamanho):
        if direcao == "h":
            linha_atual = linha
            coluna_atual = coluna + i
        else:
            linha_atual = linha + i
            coluna_atual = coluna

        if matriz[linha_atual][coluna_atual] == "O":
            input("Essa posição já está ocupada! [ENTER para continuar]")
            return False

    return True
        
            
matriz = gera_matriz()
navios = cria_navios()
try:
    while(True):
        limpa_terminal()
        mostra_mapa(matriz)
        mostra_navios(navios)
        navio = escolhe_navio()
        if navio is None:
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
            break
except Exception as e:
    print(e)

# print(len(navios.get("Submarino")))
# lista = navios.get("Submarino")
# lista.__delattr__
