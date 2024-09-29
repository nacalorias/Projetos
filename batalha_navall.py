# Importação de random para o computador posicionar suas embarcações de forma aleatória
from random import randint

# Função para gerar a matriz do tabuleiro
def tabuleiro(linha, coluna):
    tabuleiro = []
    for i in range(linha):
        tabuleiro.append(coluna * [0])
    return tabuleiro
# Função que mostra o tabuleiro do jogador
def exibir_TabuleiroJ():
    print("\nTabuleiro do Jogador")
    for i in range(5):
        print(tabuleiroJogador[i])
# Função que mostra o tabuleiro do computador
def exibir_TabuleiroC():
    print("\nTabuleiro do Computador")
    for i in range(5):
        print(tabuleiroOculto[i])
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Início dos tabuleiros do jogador e computador
tabuleiroJogador = tabuleiro(5, 10)
tabuleiroComputador = tabuleiro(5, 10)
# Início do tabuleiro que está escondido do jogador, contendo as embarcações do computador
tabuleiroOculto = tabuleiro(5, 10)

# Variáveis de string para o looping das escolhas de posições
jogador = ''
computador = ''
# Variáveis de inteiros para o looping principal
embarcacoesJogador = 5
embarcacoesComputador = 5
turno = 0 # Quando par = vez do jogador, quando ímpar = vez do computador
# Variáveis de vetores para o looping das escolhas de posições
posicaoJogador = []
posicaoComputador = []

# Posicionamento de embarcações do jogador, todas as casas com 0 são lugares vazios, e todas com 1 possuem embarcações
for i in range(5):
    # Looping para escolha das posições das embarcações do jogador
    while jogador != 'jogada':
        while True:
            linhaColuna = str(input(f'Digite a posição do seu {i + 1}º barco, sendo 0 à 4 para linha e 0 a 9 para coluna: '))
            linha, coluna = map(int, linhaColuna.split())
            if 0 <= linha < 5 and 0 <= coluna < 10:
                break
            else:
                print("Lugar inválido, por favor, tente novamente.")
        if linhaColuna not in posicaoJogador:
            tabuleiroJogador[linha][coluna] = 1
            posicaoJogador.append(linhaColuna)
            jogador = 'jogada'
        else:
            print("Você já escolheu essa posição, por favor escolha outra.")
    jogador = ''
    # Looping para escolha das posições das embarcações do computador
for i in range(5):
    while computador != 'jogada':
        linha = randint(0, 4)
        coluna = randint(0, 9)
        linhaColuna = str(linha) + str(coluna)
        if linhaColuna not in posicaoComputador and linhaColuna not in posicaoJogador:
            tabuleiroComputador[linha][coluna] = 1
            posicaoComputador.append(linhaColuna)
            computador = 'jogada'
    computador = ''

# Tabuleiros iniciais são mostrados
exibir_TabuleiroC()
exibir_TabuleiroJ()

# Loop principal do jogo, enquanto o número de embarcações no mapa for maior que 0, ele continuará rodando
while embarcacoesJogador > 0 and embarcacoesComputador > 0:
    # Ataque do jogador
    if turno % 2 == 0:
        while True:
            ataqueJogador = input("Onde deseja atacar? (0 à 4 para linha e 0 a 9 para coluna, separados por um espaço): ")
            linha, coluna = map(int, ataqueJogador.split())
            if 0 <= linha < 5 and 0 <= coluna < 10:
                break
            else:
                print("Lugar inválido, por favor, tente novamente.")
        # Se o jogador acertar uma embarcação o tabuleiro oculto é mostrado a ele, indicando que ele acertou a linha e coluna correspondente
        if tabuleiroComputador[linha][coluna] == 1:
        # Se o jogador acertar, o 0 é trocado por X no tabuleiro do computador
            tabuleiroOculto[linha][coluna] = 'X'
            # Score diminui em caso de acerto do oponente
            embarcacoesComputador -= 1
            print('Acertou! Embarcação inimiga derrubada!')
        else:
        # Se o jogador errar, o 0 é trocado por O no tabuleiro do computador
            tabuleiroOculto[linha][coluna] = 'O'
            print('Errou! Mais sorte na próxima jogada!')
    # Ataque do computador
    else:
        linha = randint(0, 4)
        coluna = randint(0, 9)
        # Verificando se a posição do ataque já foi atingida
        while tabuleiroJogador[linha][coluna] == 'X' or tabuleiroJogador[linha][coluna] == 'O':
            linha = randint(0, 4)
            coluna = randint(0, 9)
        if tabuleiroJogador[linha][coluna] == 1:
        # Se o computador acertar, o 0 é trocado por X no tabuleiro do jogador
            tabuleiroJogador[linha][coluna] = 'X'
            # Score diminui em caso de acerto do oponente
            embarcacoesJogador -= 1
            print("Inimigo acertou! Sua embarcação afundou!")
        else:
        # Se o computador errar, o 0 é trocado por O no tabuleiro do jogador
            tabuleiroJogador[linha][coluna] = 'O'
            print("Inimigo errou! É hora de atacar!")

    exibir_TabuleiroC()
    exibir_TabuleiroJ()
    print(f"Suas embarcações restantes: {embarcacoesJogador}")
    print(f"Embarcações inimigas restantes: {embarcacoesComputador}")
# Passa a vez para o próximo jogador
    turno += 1

# Final do jogo, se o score do jogador for 0 ele perde, caso contrário ele ganha
if embarcacoesJogador == 0:
    print("Todas as suas embarcações foram afundadas, você perdeu o jogo!")
else:
    print("Você derrubou todas as embarcações inimigas, parabéns pela vitória!")

print("Obrigado por jogar Batalha Naval! Jogo feito por Ana Carolina Afonso, Ana Carolina Sales e Paulo Tesseroli")
