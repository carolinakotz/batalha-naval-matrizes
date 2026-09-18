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
    return i-1

def escolhe_posicao_coluna():
    j = int(input("Digite a coluna: "))
    return j-1

def mostra_navios(navios):
    cont = 0
    for key, value in navios.items():
        for i in range(len(value)):
            print(f"{value[i]}", end="")
        cont+=1
        print(f"\t[{cont}] - {key}")
        print()

def insere_navio(matriz, navios, linha, coluna, navio, direcao):
    navio_lista = navios.get(navio) 
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
    direcao = input("Qual a direção do navio\n[H] - Horizontal\n[V] - Vertical\n")
    return direcao

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

def arruma_posicao():
    resposta = int(input("Deseja mudar a posição\n[1] - sim\n[2] - não"))
    if resposta == 1:
        return True
    return False    
     
def apaga_navio(matriz, navios_adicionados, navio, navios):
        dados_navio = navios_adicionados.get(navio)
        navio_lista = navios.get(navio)
        if dados_navio[2].lower() == "h":
            for i in range(len(navio_lista)):
                matriz[dados_navio[0]][dados_navio[1]+i] = ""
        else:
            for i in range(len(navio_lista)):
                matriz[dados_navio[0]+i][dados_navio[1]] = ""

def busca_navio(matriz, linha, coluna):
    if matriz[linha][coluna] == "O":
        return True
    return False

def atacar(matriz):
    i = escolhe_posicao_linha()
    j = escolhe_posicao_coluna()
    if busca_navio(matriz, i, j):
        matriz[i][j] = "X"
    else:
        matriz[i][j] = "X"
              
def valida_indices(indice):
    if indice >= 0 or indice <= 10:
        return True
    return False


matriz = gera_matriz()
navios = cria_navios()
navios_adicionados = {}
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
        if (len(navios_adicionados) > 0):
            if navio in navios_adicionados.keys():
                if arruma_posicao():
                    apaga_navio(matriz,navios_adicionados,navio,navios)
                    while True:
                        i = escolhe_posicao_linha()
                        j = escolhe_posicao_coluna()
                        direcao = escolhe_direcao()
                        if not insere_navio(matriz,navios,i,j,navio, direcao):
                            limpa_terminal()
                            mostra_mapa(matriz)
                            continue   
                        navios_adicionados.update({navio: [i,j,direcao]}) 
                        break
            continue
                    
        while True:
            i = escolhe_posicao_linha()
            j = escolhe_posicao_coluna()
            direcao = escolhe_direcao()
            if not insere_navio(matriz,navios,i,j,navio, direcao):
                limpa_terminal()
                mostra_mapa(matriz)
                continue    
            break
        navios_adicionados.update({navio: [i,j,direcao]})
        if len(navios_adicionados) ==4:
            resposta = input("Iniciar o jogo ?\t[s]-sim  [n]-não")
            if resposta.lower() == "n":
                continue
            else:
                break
except Exception as e:
    print(e)

