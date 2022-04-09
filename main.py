from jogador import *
from tabuleiro import *
from banco import *

if __name__ == '__main__':
    tabuleiro = Tabuleiro()
    banco = Banco()
    jogador = Jogador('Sérgio', tabuleiro, banco)

    tabuleiro.adicionar_jogador(jogador)

    while True:
        jogador.jogar_dados()
        jogador.mostrar_dinheiro()
        jogador.andar()

        jogador.comprar_propriedade()
        print('=' * 70)
