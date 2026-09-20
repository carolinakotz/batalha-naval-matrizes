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


def le_inteiro(mensagem):
    """Repete a leitura até o jogador digitar um número inteiro."""

    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")


def confirma_reposicionamento():
    """Retorna True para mudar a posição e False para manter o navio."""

    while True:
        resposta = le_inteiro(
            "Deseja mudar a posição?\n"
            "[1] - Sim\n"
            "[2] - Não\n"
        )
        if resposta == 1:
            return True
        if resposta == 2:
            return False
        print("Opção inválida! Digite 1 ou 2.")


def escolhe_navio():
    """
    Solicita uma opção numérica e retorna o nome do navio.

    Retorna '0' para sair ou None se o número não corresponder a uma opção.
    """

    navio = le_inteiro("Escolha o navio que deseja posicionar: ")
    
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
    """Solicita uma linha de 1 a 10 e retorna seu índice de 0 a 9."""

    while True:
        i = le_inteiro("Digite a linha: ")
        if valida_linha(i - 1):
            return i - 1
        print("Linha inválida! Digite um número de 1 a 10.")


def escolhe_posicao_coluna():
    """Solicita uma letra de A a J e retorna o índice da coluna de 0 a 9."""
    while True:
        j = input("Digite a coluna: ").lower()
        if valida_coluna_letra(j):
            match j:
                case "a" : return 0
                case "b" : return 1
                case "c" : return 2
                case "d" : return 3
                case "e" : return 4
                case "f" : return 5
                case "g" : return 6
                case "h" : return 7
                case "i" : return 8
                case "j" : return 9
        print("Coluna inválida!")


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
    if verifica_posicao_valida(matriz,linha,coluna,navio_lista, direcao):
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

def verifica_existencia_tabuleiro(matriz, linha, coluna):
    """Retorna True se a linha e a coluna existirem no tabuleiro."""

    return (
        0 <= linha < len(matriz)
        and 0 <= coluna < len(matriz[linha])
    )


def verifica_posicao_ocupada(matriz, linha, coluna):
    """Retorna True se a posição existir e contiver um navio."""

    return (
        verifica_existencia_tabuleiro(matriz, linha, coluna)
        and matriz[linha][coluna] == "O"
    )


def verifica_navio_cabe(matriz, linha, coluna, tamanho, direcao):
    """Verifica se a posição inicial existe e o navio cabe na direção indicada."""

    if not verifica_existencia_tabuleiro(matriz, linha, coluna):
        return False
    if direcao == "h":
        return coluna + tamanho <= len(matriz[linha])
    if direcao == "v":
        return linha + tamanho <= len(matriz)

    return False


def verifica_vizinhanca(matriz, linha, coluna):
    """Verifica se existe um navio nas oito posições vizinhas."""

    for linha_vizinha in range(linha - 1, linha + 2):
        for coluna_vizinha in range(coluna - 1, coluna + 2):
            if linha_vizinha == linha and coluna_vizinha == coluna:
                continue
            if verifica_posicao_ocupada(
                matriz, linha_vizinha, coluna_vizinha
            ):
                return True

    return False


def verifica_posicao_valida(matriz, linha, coluna, navio, direcao):
    """
    Verifica se o navio cabe sem sobrepor ou encostar em outro navio.

    Recebe índices a partir de zero e direção 'h' ou 'v'.
    Retorna True para posição válida e False para inválida.
    """
    tamanho_navio = len(navio)
    if not verifica_navio_cabe(matriz, linha, coluna, tamanho_navio, direcao):
        input("O navio não cabe nesta posição!\t[ENTER para continuar]")
        return False
    
    for _ in range(tamanho_navio):
        if verifica_posicao_ocupada(matriz, linha, coluna):
            input("Essa posição já está ocupada!\t[ENTER para continuar]")
            return False    
        if verifica_vizinhanca(matriz, linha, coluna):
            input("Posição inválida!\t[ENTER para continuar]")  
            return False   
        if direcao == "h":
            coluna += 1
        else: 
            linha += 1
    return True

def arruma_posicao(matriz,navios_adicionados,navio,navios):
    apaga_navio(matriz,navios_adicionados,navio,navios)
    escolhe_posicao(matriz, navios, navio, navios_adicionados)
 
     
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
              
def valida_linha(indice):
    if indice >= 0 and indice <= 9:
        return True
    return False

def valida_coluna_letra(j):
    colunas_validas = ("a", "b", "c", "d", "e","f","g", "h", "i", "j")
    if j in colunas_validas:
        return True
    return False

def escolhe_posicao(matriz, navios, navio, navios_adicionados): 
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


def confirma_inicio():
    """Retorna True para iniciar ou False para continuar a preparação."""

    while True:
        resposta = input(
            "Iniciar o jogo?\n"
            "[S] - Sim\n"
            "[N] - Não\n"
        ).lower()
        if resposta == "s":
            return True
        if resposta == "n":
            return False
        print("Opção inválida! Digite S ou N.")


matriz = gera_matriz()
navios = cria_navios()
navios_adicionados = {}

while True:
    limpa_terminal()
    mostra_mapa(matriz)
    mostra_navios(navios)

    navio = escolhe_navio()
    if navio is None:
        continue
    if navio == "0":
        break

    if navio in navios_adicionados:
        if confirma_reposicionamento():
            arruma_posicao(matriz, navios_adicionados, navio, navios)
        else:
            continue
    else:
        escolhe_posicao(matriz, navios, navio, navios_adicionados)

    if len(navios_adicionados) == len(navios):
        if confirma_inicio():
            break
