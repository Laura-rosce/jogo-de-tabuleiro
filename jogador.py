from random import randint


class Jogador:
    def __init__(self, nome, tabuleiro, banco):
        self.tabuleiro = tabuleiro
        self.banco = banco
        self.id = randint(0, 999999999)
        self.nome = nome
        self.propriedades = []
        self.posicao = 1
        self.dinheiro = 2558000
        self.jogadas = []
        self.volta = 0

    def __str__(self):
        return self.nome

    def jogar_dados(self):
        self.jogadas = []
        jogando = True
        while jogando:
            dado_1 = randint(1, 6)
            dado_2 = randint(1, 6)

            print(f'E os valores são... {dado_1} e {dado_2}!')

            self.jogadas.append([dado_1, dado_2])

            if dado_1 == dado_2:
                if len(self.jogadas) == 3:
                    jogada_3 = self.jogadas[2]
                    for dado in jogada_3:
                        if jogada_3.count(dado) == 2:
                            print(f'Que pena, {self} tirou números iguais três vezes seguidas... Vá para a detenção!')
                            self.posicao = 11
                            self.jogadas = []
                            jogando = False
                            break
                else:
                    print(f'{self} tirou números iguais, jogue novamente!')
                    continue
            else:
                break

    def andar(self):
        posicoes_andadas = 0
        for jogada in self.jogadas:
            posicoes_andadas += sum(jogada)

        if posicoes_andadas == 0:
            if self.posicao == 11:
                print(f'{self} está preso na cadeia.')
            else:
                print(f'{self} continua na posição {self.posicao}.')
        else:
            print(f'{self} estava na posição {self.posicao}.')

            self.posicao += posicoes_andadas

            if self.posicao > 40:
                self.posicao -= 40
                self.volta += 1
                self.dinheiro += 200000

                print(f'{self} agora está na posição {self.posicao}.')
                print(f'{self} completou {self.volta} volta(s).')
                print(f'{self} recebeu $ 200000 do banco.')
            else:
                print(f'{self} agora está na posição {self.posicao}.')

        self.tabuleiro.mostrar_nome_posicao(self)

    def mostrar_dinheiro(self):
        print(f'{self} está com $ {self.dinheiro} na conta.')

    def comprar_propriedade(self):
        posicoes_nao_compraveis = [1, 7, 9, 11, 12, 17, 21, 25, 28, 31, 33, 39]

        if self.posicao in posicoes_nao_compraveis:
            print(f'A posição {self.posicao} não é uma propriedade.')
        else:
            if self.tabuleiro.posicoes[self.posicao][2] is None:
                self.tabuleiro.mostrar_preco_posicao(self)
                while True:
                    escolha = input('Deseja comprar esta propriedade? (S/N): ').upper()
                    if escolha == 'S':
                        self.banco.vender_propriedade(self)
                        self.mostrar_propriedades()
                        break
                    elif escolha == 'N':
                        break
                    else:
                        print('Resposta inválida.')
            else:
                print('Esta propriedade está indisponível para compra.')
                self.tabuleiro.verificar_dono(self)

    def mostrar_propriedades(self):
        print(f'Propriedades de {self}:')
        for propriedade in self.propriedades:
            print(f'{propriedade} — {self.tabuleiro.posicoes[propriedade][0]}')
