import os
import subprocess


def limpa_terminal():
    """Limpa o terminal usando o comando adequado ao sistema operacional."""

    if os.name == "nt":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear")


def gera_matriz():
    """Cria e retorna uma matriz 10x10 preenchida com strings vazias."""

    linha = []
    for i in range(10):
        coluna = []
        for j in range(10):
            coluna.append("")
        linha.append(coluna)

    return linha


def mostra_mapa(matriz):
    """Exibe o tabuleiro com bordas e numeração das linhas e colunas."""

    print("    A   B   C   D   E   F   G   H   I   J")

    for i in range(len(matriz)):
        print("  " + "----" * len(matriz) + "-")
        print(f"{i + 1:2}|", end="")
        for j in range(len(matriz[i])):
            print(f" {matriz[i][j]:1} |", end="")
        print()

    print("  " + "----" * len(matriz) + "-")


def cria_navios():
    """Retorna um dicionário em que cada 'O' representa uma parte do navio."""

    navios = {
        "Submarino": ["O", "O"],
        "Contratorpedeiro": ["O", "O", "O"],
        "Navio-tanque": ["O", "O", "O", "O"],
        "Porta-aviões": ["O", "O", "O", "O", "O"]
    }

    return navios


def escolhe_navio():
    """
    Solicita uma opção numérica e retorna o nome do navio.

    Retorna '0' para sair ou None se o número não corresponder a uma opção.
    """

    navio = int(input("Escolha o navio que deseja posicionar: "))

    match navio:
        case 0:
            return "0"
        case 1:
            return "Submarino"
        case 2:
            return "Contratorpedeiro"
        case 3:
            return "Navio-tanque"
        case 4:
            return "Porta-aviões"
        case _:
            print("Não é uma escolha válida!")

    return None


def escolhe_posicao_linha():
    """Solicita e retorna a linha como inteiro, sem validar seus limites."""

    i = int(input("Digite a linha: "))
    return i-1


def escolhe_posicao_coluna():
    """Solicita e retorna a coluna como inteiro, sem validar seus limites."""

    j = int(input("Digite a coluna: "))
    return j-1


def mostra_navios(navios):
    """Exibe os nomes, as partes e as opções numéricas dos navios."""

    cont = 0
    for key, value in navios.items():
        for i in range(len(value)):
            print(f"{value[i]}", end="")
        cont += 1
        print(f"\t[{cont}] - {key}")
        print()

def insere_navio(matriz, navios, linha, coluna, navio, direcao):
    navio_lista = navios.get(navio) 
    if verifica_posicao_invalida(matriz,linha,coluna,navio_lista, direcao):
        match direcao.lower():
            case "v":
                for i in range(len(navio_lista)):
                    matriz[linha + i][coluna] = navio_lista[i]
            case "h":
                for i in range(len(navio_lista)):
                    matriz[linha][coluna + i] = navio_lista[i]
        return True
    else:
        return False


def escolhe_direcao():
    """Repete a pergunta até receber H ou V e retorna 'h' ou 'v'."""

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
    """
    Verifica se o navio cabe no tabuleiro e não sobrepõe outro navio.

    Recebe índices a partir de zero e direção 'h' ou 'v'.
    Retorna True para posição válida e False para inválida.
    Permite navios encostados.
    """

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
              
        
matriz = gera_matriz()
navios = cria_navios()
navios_adicionados = {}
try:
    while True:
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
        if len(navios_adicionados == 4):
            resposta = input("Iniciar o jogo ?\t[s]-sim  [n]-não")
            if resposta.lower() == "n":
                continue
            else:
                break
except Exception as e:
    print(e)

