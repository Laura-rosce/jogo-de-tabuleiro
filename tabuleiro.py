class Tabuleiro:
    def __init__(self):
        self.posicoes = {
            1: ["Início", None, None],
            2: ["Jardim Botânico", 100000, None],
            3: ["Avenida Niemeyer", 75000, None],
            4: ["Companhia Petrolífera", 200000, None],
            5: ["Avenida Beira Mar", 60000, None],
            6: ["Avenida Juscelino Kubitschek", 240000, None],
            7: ["Sorte Revés", None, None],
            8: ["Rua Oscar Freire", 220000, None],
            9: ["Restituição do Imposto de Renda", None, None],
            10: ["Avenida Ibirapuera", 220000, None],
            11: ["Cadeia", None, None],
            12: ["Sorte Revés", None, None],
            13: ["Praça da Sé", 200000, None],
            14: ["Rua da Consolação", 180000, None],
            15: ["Central de Força e Luz", 200000, None],
            16: ["Viaduto do Chá", 180000, None],
            17: ["Receita Federal", None, None],
            18: ["Higienópolis", 400000, None],
            19: ["Jardins", 350000, None],
            20: ["Avenida São João", 120000, None],
            21: ["Feriado", None, None],
            22: ["Avenida Ipiranga", 100000, None],
            23: ["Companhia de Água e Saneamento", 200000, None],
            24: ["Companhia de Mineração", 200000, None],
            25: ["Sorte Revés", None, None],
            26: ["Avenida Recife", 140000, None],
            27: ["Avenida Paulista", 160000, None],
            28: ["Sorte Revés", None, None],
            29: ["Ponte do Guaíba", 140000, None],
            30: ["Pontocom", 150000, None],
            31: ["Camburão", None, None],
            32: ["Praça dos Três Poderes", 320000, None],
            33: ["Sorte Revés", None, None],
            34: ["Praça Castro Alves", 300000, None],
            35: ["Avenida do Contorno", 300000, None],
            36: ["Ponte Rio-Niterói", 280000, None],
            37: ["Créditos de Carbono", 150000, None],
            38: ["Barra da Tijuca", 260000, None],
            39: ["Sorte Revés", None, None],
            40: ["Marina da Glória", 260000, None],
        }
        self.jogadores = {}

    def adicionar_jogador(self, jogador):
        self.jogadores.update({jogador.id: jogador})

    def mostrar_nome_posicao(self, jogador):
        nome = self.posicoes[jogador.posicao][0]
        print(f'Posição {jogador.posicao}: {nome}.')

    def mostrar_preco_posicao(self, jogador):
        print(f'Preço: $ {self.posicoes[jogador.posicao][1]}.')

    def verificar_dono(self, jogador):
        id_dono = self.posicoes[jogador.posicao][2]
        nome_dono = self.jogadores[id_dono]
        print(f'Dono: {nome_dono}.')
