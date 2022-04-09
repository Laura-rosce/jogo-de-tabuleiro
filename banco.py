class Banco:
    def __init__(self):
        self.dinheiro = float('inf')

    @staticmethod
    def vender_propriedade(jogador):
        if jogador.dinheiro >= jogador.tabuleiro.posicoes[jogador.posicao][1]:
            jogador.propriedades.append(jogador.posicao)

            jogador.tabuleiro.posicoes[jogador.posicao][2] = jogador.id
            jogador.dinheiro -= jogador.tabuleiro.posicoes[jogador.posicao][1]

            print('Propriedade comprada com sucesso!')
            print(f'Valor: $ {jogador.tabuleiro.posicoes[jogador.posicao][1]}.')

            jogador.mostrar_dinheiro()
        else:
            print(f'{jogador} não tem dinheiro suficiente para comprar esta propriedade.')
