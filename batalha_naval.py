import os
import random
import subprocess
 
def limpa_terminal():
    "Limpa o terminal de acordo com a sistema operacional"
 
    if os.name == "nt":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear")
 
def gera_matriz():
    "Cria e retorna uma matriz 10x10 preenchida com strings vazias."
 
    linha = []
    for i in range(10):
        coluna = []
        for j in range(10):
            coluna.append("")
        linha.append(coluna)
 
    return linha
 
 
def monta_linhas_mapa(matriz, esconder_navios):
    "Monta as linhas de texto do tabuleiro (bordas e numeração)."
    "Com esconder_navios=True, as partes de navio ainda intactas ('O') aparecem vazias, o que serve para exibir o mapa do adversário."
    
 
    linhas = ["    A   B   C   D   E   F   G   H   I   J"]
 
    for i in range(len(matriz)):
        linhas.append("  " + "----" * len(matriz) + "-")
        texto = f"{i + 1:2}|"
        for j in range(len(matriz[i])):
            celula = matriz[i][j]
            if esconder_navios and celula == "O":
                celula = ""
            texto += f" {celula:1} |"
        linhas.append(texto)
 
    linhas.append("  " + "----" * len(matriz) + "-")
 
    return linhas
 
 
def mostra_mapa(matriz):
    "Mostra o tabuleiro com bordas e numeração das linhas e colunas."
 
    linhas = monta_linhas_mapa(matriz, False)
    for linha in linhas:
        print(linha)
 
def cria_navios():
    "Retorna um dicionário que cada 'O' representa uma parte do navio."
 
    navios = {
        "Submarino": ["O", "O"],
        "Contratorpedeiro": ["O", "O", "O"],
        "Navio-tanque": ["O", "O", "O", "O"],
        "Porta-aviões": ["O", "O", "O", "O", "O"]
    }
 
    return navios
 
 
def verifica_navio_afundado(partes):
    "Retorna True se todas as partes do navio for atingidas ('X')."
 
    for parte in partes:
        if parte == "O":
            return False
 
    return True
 
 
def verifica_frota_destruida(navios):
    "Retorna True se todos os navios do dicionário for afundados."
 
    for nome, partes in navios.items():
        if not verifica_navio_afundado(partes):
            return False
 
    return True
 
 
def monta_linhas_frota(navios, mostra_opcoes, esconder_acertos):
    """
    Monta as linhas de texto com o estado de cada navio.

    'O' é uma parte intacta e 'X' é uma parte atingida. Com mostra_opcoes=True
    cada navio recebe seu número de escolha. Com esconder_acertos=True só
    aparece o resultado final: navios ainda não afundados são exibidos como
    intactos, sem revelar quantas partes já foram atingidas.
    """
 
    linhas = []
    cont = 0
 
    for nome, partes in navios.items():
        cont += 1
        afundado = verifica_navio_afundado(partes)
 
        texto = ""
        for parte in partes:
            if esconder_acertos and not afundado:
                texto += "O"
            else:
                texto += parte
 
        texto = f"{texto:6}"
        if mostra_opcoes:
            texto += f"[{cont}] - {nome}"
        else:
            texto += nome
            if afundado:
                texto += " (afundado)"
        linhas.append(texto)
 
    return linhas
 
 
def mostra_navios(navios):
    "Exibe os nomes, as partes e as opções numéricas dos navios."
 
    linhas = monta_linhas_frota(navios, True, False)
    for linha in linhas:
        print(linha)
        print()
 
 
def encontra_navio(navios, navios_adicionados, linha, coluna):
    """
    Associa uma posição do mapa ao navio que a ocupa.
 
    Retorna um dicionário com o 'nome' do navio e o 'indice' da parte
    atingida, ou 'None' se nenhum navio ocupar a posição.
    """
 
    for nome, dados in navios_adicionados.items():
        for i in range(len(navios[nome])):
            if dados[2] == "h":
                l = dados[0]
                c = dados[1] + i
            else:
                l = dados[0] + i
                c = dados[1]
            if l == linha and c == coluna:
                return {"nome": nome, "indice": i}
 
    return None
 
def le_inteiro(mensagem):
    "Repete a leitura até o jogador digitar um número inteiro."
 
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
 
 
def confirma_reposicionamento():
    "Retorna True para mudar a posição e False para manter o navio."
 
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
            input("Não é uma escolha válida!\t[ENTER para continuar]")
 
    return None
 
 
def escolhe_posicao_linha():
    "Solicita uma linha de 1 a 10 e retorna seu índice de 0 a 9."
 
    while True:
        i = le_inteiro("Digite a linha: ")
        if valida_linha(i - 1):
            return i - 1
        print("Linha inválida! Digite um número de 1 a 10.")
 
 
def escolhe_posicao_coluna():
    "Solicita uma letra de A a J e retorna o índice da coluna de 0 a 9."
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
 
 
def escolhe_direcao():
    "Repete a pergunta até receber H ou V e retorna 'h' ou 'v'."
 
    while True:
        direcao = input(
            "Qual a direção do navio?\n"
            "[H] - Horizontal\n"
            "[V] - Vertical\n"
        ).lower()
 
        if direcao == "h" or direcao == "v":
            return direcao
 
        print("Direção inválida! Digite H ou V.")
 
 
def valida_linha(indice):
    if indice >= 0 and indice <= 9:
        return True
    return False
 
 
def valida_coluna_letra(j):
    colunas_validas = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
    if j in colunas_validas:
        return True
    return False
 
 
def confirma_inicio():
    "Retorna True para iniciar ou False para continuar a preparação."
 
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
 
 
def avisa_erro(mensagem, avisa):
    "Mostra a mensagem e espera ENTER, a menos que avisa seja False."
 
    if avisa:
        input(f"{mensagem}\t[ENTER para continuar]")
 
 
def verifica_existencia_tabuleiro(matriz, linha, coluna):
    "Retorna True se a linha e a coluna existirem no tabuleiro."
 
    return (
        0 <= linha < len(matriz)
        and 0 <= coluna < len(matriz[linha])
    )
 
 
def verifica_posicao_ocupada(matriz, linha, coluna):
    "Retorna True se a posição existir e contiver um navio."
 
    return (
        verifica_existencia_tabuleiro(matriz, linha, coluna)
        and matriz[linha][coluna] == "O"
    )
 
 
def verifica_navio_cabe(matriz, linha, coluna, tamanho, direcao):
    "Verifica se a posição inicial existe e o navio cabe na direção indicada."
 
    if not verifica_existencia_tabuleiro(matriz, linha, coluna):
        return False
    if direcao == "h":
        return coluna + tamanho <= len(matriz[linha])
    if direcao == "v":
        return linha + tamanho <= len(matriz)
 
    return False
 
 
def verifica_vizinhanca(matriz, linha, coluna):
    "Verifica se existe um navio nas oito posições vizinhas."
 
    for linha_vizinha in range(linha - 1, linha + 2):
        for coluna_vizinha in range(coluna - 1, coluna + 2):
            if linha_vizinha == linha and coluna_vizinha == coluna:
                continue
            if verifica_posicao_ocupada(
                matriz, linha_vizinha, coluna_vizinha
            ):
                return True
 
    return False
 
 
def verifica_posicao_valida(matriz, linha, coluna, navio, direcao, avisa):
    """
    Verifica se o navio cabe sem sobrepor ou encostar em outro navio.
 
    Recebe índices a partir de zero e direção 'h' ou 'v'.
    Retorna True para posição válida e False para inválida.
    Com avisa=False nenhuma mensagem é exibida (usado pelo bot).
    """
    tamanho_navio = len(navio)
    if not verifica_navio_cabe(matriz, linha, coluna, tamanho_navio, direcao):
        avisa_erro("O navio não cabe nesta posição!", avisa)
        return False
 
    for _ in range(tamanho_navio):
        if verifica_posicao_ocupada(matriz, linha, coluna):
            avisa_erro("Essa posição já está ocupada!", avisa)
            return False
        if verifica_vizinhanca(matriz, linha, coluna):
            avisa_erro("Posição inválida!", avisa)
            return False
        if direcao == "h":
            coluna += 1
        else:
            linha += 1
    return True
 
 
def insere_navio(matriz, navios, linha, coluna, navio, direcao, avisa):
    "Coloca o navio no mapa se a posição for válida e retorna True/False."
 
    navio_lista = navios.get(navio)
    if verifica_posicao_valida(matriz, linha, coluna, navio_lista, direcao, avisa):
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
 
 
def apaga_navio(matriz, navios_adicionados, navio, navios):
    dados_navio = navios_adicionados.get(navio)
    navio_lista = navios.get(navio)
    if dados_navio[2].lower() == "h":
        for i in range(len(navio_lista)):
            matriz[dados_navio[0]][dados_navio[1] + i] = ""
    else:
        for i in range(len(navio_lista)):
            matriz[dados_navio[0] + i][dados_navio[1]] = ""
 
 
def escolhe_posicao(matriz, navios, navio, navios_adicionados):
    "Pede linha, coluna e direção até o navio ser inserido em local válido."
 
    while True:
        i = escolhe_posicao_linha()
        j = escolhe_posicao_coluna()
        direcao = escolhe_direcao()
        if not insere_navio(matriz, navios, i, j, navio, direcao, True):
            limpa_terminal()
            mostra_mapa(matriz)
            continue
        break
    navios_adicionados.update({navio: [i, j, direcao]})
 
 
def arruma_posicao(matriz, navios_adicionados, navio, navios):
    apaga_navio(matriz, navios_adicionados, navio, navios)
    escolhe_posicao(matriz, navios, navio, navios_adicionados)
 
 
def posiciona_navios_aleatorio(matriz, navios, navios_adicionados):
    "Posiciona todos os navios em locais aleatórios e válidos (usado pelo bot)."
 
    for nome in navios:
        while True:
            linha = random.randint(0, len(matriz) - 1)
            coluna = random.randint(0, len(matriz[0]) - 1)
            if random.randint(0, 1) == 0:
                direcao = "h"
            else:
                direcao = "v"
            if insere_navio(matriz, navios, linha, coluna, nome, direcao, False):
                navios_adicionados[nome] = [linha, coluna, direcao]
                break
 
 
def busca_navio(matriz, linha, coluna):
    if matriz[linha][coluna] == "O":
        return True
    return False
 
def ja_atacada(matriz, linha, coluna):
    "Retorna True se a posição já recebeu um tiro (acerto 'X' ou água '~')."
 
    return matriz[linha][coluna] == "X" or matriz[linha][coluna] == "~"
 
def recebe_ataque(matriz, navios, navios_adicionados, linha, coluna):
    """
    Aplica um tiro no mapa e nos navios associados a ele.
 
    Se acertar, marca 'X' no mapa e na parte correspondente do navio.
    Se errar, marca '~' no mapa.
    Retorna um dicionário com 'linha', 'coluna', 'acertou', 'navio' (nome do
    navio atingido ou None) e 'afundou'.
    """
 
    resultado = {
        "linha": linha,
        "coluna": coluna,
        "acertou": False,
        "navio": None,
        "afundou": False
    }
 
    if not busca_navio(matriz, linha, coluna):
        matriz[linha][coluna] = "~"
        return resultado
 
    matriz[linha][coluna] = "X"
    parte = encontra_navio(navios, navios_adicionados, linha, coluna)
    navios[parte["nome"]][parte["indice"]] = "X"
 
    resultado["acertou"] = True
    resultado["navio"] = parte["nome"]
    resultado["afundou"] = verifica_navio_afundado(navios[parte["nome"]])
 
    return resultado
 
 
def atacar(matriz, navios, navios_adicionados):
    """
    Lê a posição do ataque do jogador, impedindo tiros repetidos.
 
    Retorna o dicionário de resultado gerado por recebe_ataque.
    """
 
    while True:
        linha = escolhe_posicao_linha()
        coluna = escolhe_posicao_coluna()
 
        if ja_atacada(matriz, linha, coluna):
            print("Você já atacou essa posição! Escolha outra.")
            continue
 
        return recebe_ataque(matriz, navios, navios_adicionados, linha, coluna)
 
 
def formata_posicao(linha, coluna):
    "Converte índices em texto, por exemplo (0, 2) -> 'C1'."
 
    return f"{'ABCDEFGHIJ'[coluna]}{linha + 1}"
 
 
def descreve_ataque(atacante, resultado):
    "Monta a mensagem que resume o resultado de um ataque."
 
    posicao = formata_posicao(resultado["linha"], resultado["coluna"])
 
    if not resultado["acertou"]:
        texto = "acertou a água."
    elif resultado["afundou"]:
        texto = f"afundou o {resultado['navio']}!"
    else:
        texto = "acertou um navio!"
 
    return f"{atacante} atacou {posicao} e {texto}"
 
 
def cria_estado_bot():
    """
    Cria a memória do bot.
 
    'acertos': posições [linha, coluna] atingidas do navio que ele está
    perseguindo.
    'descartadas': matriz que marca com 'D' as posições em volta de navios
    afundados. Como os navios não podem se encostar, nenhuma delas guarda
    outro navio.
    """
 
    return {"acertos": [], "descartadas": gera_matriz()}
 
 
def posicao_livre(matriz, linha, coluna):
    "Retorna True se a posição existe no tabuleiro e ainda não foi atacada."
 
    return (
        verifica_existencia_tabuleiro(matriz, linha, coluna)
        and not ja_atacada(matriz, linha, coluna)
    )
 
 
def sorteia(lista):
    "Retorna um elemento aleatório da lista."
 
    return lista[random.randint(0, len(lista) - 1)]
 
 
def anda_ate_fim_do_navio(matriz, linha, coluna, passo_linha, passo_coluna):
    """
    Anda a partir de um acerto enquanto houver partes atingidas ('X').
 
    Retorna a primeira posição [linha, coluna] depois da última parte.
    """
 
    while (
        verifica_existencia_tabuleiro(matriz, linha, coluna)
        and matriz[linha][coluna] == "X"
    ):
        linha += passo_linha
        coluna += passo_coluna
 
    return [linha, coluna]
 
 
def escolhe_alvo_bot(matriz, estado):
    """
    Escolhe a posição [linha, coluna] do próximo tiro do bot no mapa do jogador.
 
    - Perseguição: depois de acertar, testa as posições ao redor do acerto.
      Com dois ou mais acertos a direção do navio já é conhecida, então o
      bot continua na mesma linha ou coluna, pelas pontas.
    - Caça: sem nenhum navio ferido, atira em posições aleatórias no padrão
      de tabuleiro de xadrez. Como o menor navio tem 2 partes, esse padrão
      não deixa nenhum navio escapar e usa metade dos tiros.
    """
 
    acertos = estado["acertos"]
    candidatos = []
 
    if len(acertos) == 1:
        l = acertos[0][0]
        c = acertos[0][1]
        vizinhos = [[l - 1, c], [l + 1, c], [l, c - 1], [l, c + 1]]
        for p in vizinhos:
            if posicao_livre(matriz, p[0], p[1]):
                candidatos.append(p)
    elif len(acertos) > 1:
        l = acertos[0][0]
        c = acertos[0][1]
        if acertos[0][0] == acertos[1][0]:
            direcoes = [[0, -1], [0, 1]]
        else:
            direcoes = [[-1, 0], [1, 0]]
        for d in direcoes:
            p = anda_ate_fim_do_navio(matriz, l, c, d[0], d[1])
            if posicao_livre(matriz, p[0], p[1]):
                candidatos.append(p)
 
    if len(candidatos) > 0:
        return sorteia(candidatos)
 
    xadrez = []
    livres = []
    qualquer = []
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if posicao_livre(matriz, l, c):
                qualquer.append([l, c])
                if estado["descartadas"][l][c] == "":
                    livres.append([l, c])
                    if (l + c) % 2 == 0:
                        xadrez.append([l, c])
 
    if len(xadrez) > 0:
        return sorteia(xadrez)
    if len(livres) > 0:
        return sorteia(livres)
    return sorteia(qualquer)
 
 
def atualiza_estado_bot(estado, resultado):
    "Atualiza a memória do bot com o resultado do último tiro."
 
    if resultado["acertou"]:
        estado["acertos"].append([resultado["linha"], resultado["coluna"]])
 
        if resultado["afundou"]:
            for acerto in estado["acertos"]:
                for dl in range(-1, 2):
                    for dc in range(-1, 2):
                        l = acerto[0] + dl
                        c = acerto[1] + dc
                        if verifica_existencia_tabuleiro(estado["descartadas"], l, c):
                            estado["descartadas"][l][c] = "D"
            estado["acertos"] = []
 
 
def mostra_tabuleiros(matriz_jogador, navios_jogador, matriz_bot, navios_bot,
                      revela_bot):
    "Exibe lado a lado o mapa do jogador e o mapa do bot, com suas frotas."
 
    mapa_jogador = monta_linhas_mapa(matriz_jogador, False)
    mapa_bot = monta_linhas_mapa(matriz_bot, not revela_bot)
    frota_jogador = monta_linhas_frota(navios_jogador, False, False)
    frota_bot = monta_linhas_frota(navios_bot, False, not revela_bot)
 
    print("O = navio | X = acerto | ~ = água\n")
    print(f"{'    SEU MAPA':43}     {'    MAPA DO BOT'}")
    print()
 
    i = 0
    while i < len(mapa_jogador):
        print(f"{mapa_jogador[i]:43}     {mapa_bot[i]}")
        i += 1
    print()
 
    i = 0
    while i < len(frota_jogador):
        print(f"{frota_jogador[i]:43}     {frota_bot[i]}")
        i += 1
    print()
 
 
def fase_preparacao(matriz, navios, navios_adicionados):
    """
    Deixa o jogador posicionar seus navios.
 
    Retorna True quando o jogador confirma o início do jogo e False se ele
    escolher voltar ao menu.
    """
 
    while True:
        limpa_terminal()
        mostra_mapa(matriz)
        mostra_navios(navios)
        print("[0] - Voltar ao menu\n")
 
        if len(navios_adicionados) == len(navios) and confirma_inicio():
            return True
 
        navio = escolhe_navio()
        if navio is None:
            continue
        if navio == "0":
            return False
 
        if navio in navios_adicionados:
            if confirma_reposicionamento():
                arruma_posicao(matriz, navios_adicionados, navio, navios)
        else:
            escolhe_posicao(matriz, navios, navio, navios_adicionados)
 
 
def joga_partida():
    "Executa uma partida completa: preparação, turnos e resultado final."
 
    matriz_jogador = gera_matriz()
    navios_jogador = cria_navios()
    posicoes_jogador = {}
 
    if not fase_preparacao(matriz_jogador, navios_jogador, posicoes_jogador):
        return
 
    matriz_bot = gera_matriz()
    navios_bot = cria_navios()
    posicoes_bot = {}
    posiciona_navios_aleatorio(matriz_bot, navios_bot, posicoes_bot)
    estado_bot = cria_estado_bot()
 
    mensagens = ["O bot posicionou os navios. Bom jogo!"]
 
    while True:
        limpa_terminal()
        mostra_tabuleiros(
            matriz_jogador, navios_jogador, matriz_bot, navios_bot, False
        )
        for mensagem in mensagens:
            print(mensagem)
        print()
 
        # Turno do jogador
        resultado = atacar(matriz_bot, navios_bot, posicoes_bot)
        mensagens = [descreve_ataque("Você", resultado)]
        if verifica_frota_destruida(navios_bot):
            mensagem_final = "Parabéns, você afundou toda a frota do bot!"
            break
 
        # Turno do bot
        alvo = escolhe_alvo_bot(matriz_jogador, estado_bot)
        resultado = recebe_ataque(
            matriz_jogador, navios_jogador, posicoes_jogador, alvo[0], alvo[1]
        )
        atualiza_estado_bot(estado_bot, resultado)
        mensagens.append(descreve_ataque("O bot", resultado))
        if verifica_frota_destruida(navios_jogador):
            mensagem_final = "Que pena, o bot afundou toda a sua frota!"
            break
 
    limpa_terminal()
    mostra_tabuleiros(
        matriz_jogador, navios_jogador, matriz_bot, navios_bot, True
    )
    for mensagem in mensagens:
        print(mensagem)
    print(f"\n{mensagem_final}\n")
    input("[ENTER para voltar ao menu]")
 
# Menu

def mostra_menu():
    "Exibe as opções do menu principal."
 
    print(
        "===== BATALHA NAVAL =====\n"
        "\n"
        "[1] - Jogar contra o bot\n"
        "[2] - Como jogar\n"
        "[0] - Sair\n"
    )
 
 
def mostra_regras():
    "Exibe as regras do jogo e espera o jogador voltar ao menu."
 
    limpa_terminal()
    print(
        "===== COMO JOGAR =====\n"
        "\n"
        "- Cada jogador tem 4 navios: Submarino (2 partes),\n"
        "  Contratorpedeiro (3), Navio-tanque (4) e Porta-aviões (5).\n"
        "- Os navios não podem se sobrepor nem se encostar,\n"
        "  nem mesmo na diagonal.\n"
        "- Você posiciona os seus navios. O bot posiciona os dele\n"
        "  aleatoriamente e em segredo.\n"
        "- A cada rodada você ataca uma posição do mapa do bot e,\n"
        "  em seguida, o bot ataca uma posição do seu mapa.\n"
        "- Legenda: O = parte de navio, X = acerto, ~ = água.\n"
        "- Vence quem afundar todos os navios do adversário primeiro.\n"
    )
    input("[ENTER para voltar ao menu]")
 
 
def main():
    "Mantém o menu principal ativo até o jogador escolher sair."
 
    while True:
        limpa_terminal()
        mostra_menu()
 
        opcao = le_inteiro("Escolha uma opção: ")
        match opcao:
            case 1:
                joga_partida()
            case 2:
                mostra_regras()
            case 0:
                print("Até a próxima!")
                break
            case _:
                input("Opção inválida!\t[ENTER para continuar]")
 
 
main()