import os
import subprocess


def limpa_termianl():
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
            print("-", end="")
        print()
        for j in range(9):
            print(f" {matriz[i][j]}  |", end="")
        print()

def cria_navios():

    navios = {
        "Submarino": ["O", "O"],
        "Contratorpedeiro": ["O", "O", "O"],
        "Navio-tanque": ["O", "O", "O", "O"],
        "Porta-aviões": ["O", "O", "O", "O", "O"]
    }
    return navios

def escolhe_navio():
    # TRATAMENTO DE ERRO
    try:
        navio = int(input("Escolha o navio que deseja posicionar: "))
    except ValueError:
        print("Erro! Digite apenas números.")
        input("[ENTER para continuar]")
        return None

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
    # TRATAMENTO DE ERRO
    try:
        i = int(input("Digite a linha: "))
    except ValueError:
        print("Erro! Digite apenas números.")
        input("[ENTER para continuar]")
        return None
    return i

def escolhe_posicao_coluna():
    # TRATAMENTO DE ERRO
    try:
        j = int(input("Digite a coluna: "))
    except ValueError:
        print("Erro! Digite apenas números.")
        input("[ENTER para continuar]")
        return None
    return j

def mostra_navios(navios):
    cont = 0
    for key, value in navios.items():
        for i in range(len(value)):
            print(f"{value[i]}", end="")
        cont += 1
        print(f"\t[{cont}] - {key}")
        print()

def insere_navio(matriz, navios, linha, coluna, navio):
    value = navios.get(navio)
    direcao = escolhe_direcao()
    if verifica_posicao_invalida(matriz, linha, coluna):
        match direcao.lower():
            case "v":
                for i in range(len(value)):
                    matriz[linha+i][coluna] = value[i]
            case "h":
                for i in range(len(value)):
                    matriz[linha][coluna+i] = value[i]

        return True
    else:
        return False

def escolhe_direcao():
    direcao = input(
        "Qual a direção do navio\n"
        "[H] - Horizontal\n"
        "[V] - Vertical\n"
    )

    return direcao

def verifica_posicao_invalida(matriz, linha, coluna):

    if matriz[linha][coluna] == "O":
        input(
            "Essa posição já está ocupada! "
            "Digite outra posição.\t"
            "[ENTER para continuar]"
        )
        return False

    elif matriz[linha][coluna+1] == "O" or matriz[linha][coluna-1] == "O":
        input(
            "Posição inválida!\t"
            "[ENTER para continuar] "
        )
        return False

    return True

matriz = gera_matriz()
navios = cria_navios()

try:
    while(True):
        limpa_termianl()
        mostra_mapa(matriz)
        mostra_navios(navios)
        navio = escolhe_navio()
        if navio == None:
            continue
        if navio == "0":
            break
        while True:
            i = escolhe_posicao_linha()
            # ADICIONADO PARA O TRATAMENTO DE ERRO
            if i == None:
                continue
            j = escolhe_posicao_coluna()
            # ADICIONADO PARA O TRATAMENTO DE ERRO
            if j == None:
                continue
            if not insere_navio(
                matriz,
                navios,
                i-1,
                j-1,
                navio
            ):
                limpa_termianl()
                mostra_mapa(matriz)
                continue
            break
except Exception as e:
    print(e)


# print(len(navios.get("Submarino")))

# lista = navios.get("Submarino")

# lista.__delattr__