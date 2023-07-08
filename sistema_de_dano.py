import random


class Jogador:
    def __init__(self, vida, aura, dano):
        self.vida = vida
        self.aura = aura
        self.dano = dano
        self.vivo = True

    def informacoes(self):  # esse método vai informar tudo que for relevante para o jogador
        print(f'vida: {self.vida}')
        print(f'aura: {self.aura}')
        print(f'dano: {self.dano}')
        print('está vivo' if self.vivo else 'está morto')

    def reduzirVidaInimigo(self, dano, tipo_arma, pessoa_contra):  # esse método agirá caso o jogador receba algum dano
        match tipo_arma:
            case 'cortante':  # ataca a aura de forma direta
                # se sobrar dano, metade vai para vida
                if pessoa_contra.aura > 0 and dano < pessoa_contra.aura:
                    pessoa_contra.aura -= dano

                elif 0 < pessoa_contra.aura < dano:
                    sobra_cortante = pessoa_contra.aura - dano
                    pessoa_contra.vida -= (abs(sobra_cortante) // 2)
                    # abs retorna o valor absoluto do número, tipo módulo

                else:
                    pessoa_contra.vida -= dano

            case 'perfurante':  # ataca tanto a aura quando a vida, a vida tem menos dano que a aura
                # se a aura acabar e ainda tiver na vida, metade do que sobrar vai pra vida
                if pessoa_contra.vida and pessoa_contra.aura > 0:  # se vida e aura maires que o dano
                    if dano % 2 == 0:
                        pessoa_contra.vida -= dano // 2
                        pessoa_contra.aura -= dano // 2
                    else:
                        pessoa_contra.vida -= dano // 2
                        pessoa_contra.aura -= dano // 2 + 1

            case 'concussão':  # ataca a vida, independente da aura
                if pessoa_contra.vida > 0:
                    pessoa_contra.vida -= dano

        # essa é a última ação do método reduzirVida
        self.vida = self.vida if self.vida > 0 else 0  # se ficar abaixo de 0 ela será 0 automaticamente
        self.aura = self.aura if self.aura > 0 else 0  # se ficar abaixo de 0 ela será 0 automaticamente
        self.vivo = self.vivo if self.vida > 0 else False  # estará vivo se a vida for positiva


class Inimigo(Jogador):
    def __init__(self, vida, aura, dano):
        super().__init__(vida, aura, dano)
        self.vivo = True


armas_padrao = {
    1: 'cortante',
    2: 'perfurante',
    3: 'concussão'
}
while True:
    try:  # tratando possíveis erros que possam acontecer
        arma_jogador = int(input('Escolha uma das armas:'
                                 '\n[1] Cortante'
                                 '\n[2] Perfurante'
                                 '\n[3] Concussão'
                                 '\n>> ').strip().lower())  # ‘strip’ tira espaços antes e depois do que for digitado

        if arma_jogador in armas_padrao:
            arma_jogador = armas_padrao[arma_jogador]
            break
        else:
            print('escolha uma arma dentre as possíveis...')

    except ValueError:  # se ele digitar uma letra ou outra coisa
        print('escreva um número...')

aura_padrao = 100
vida_padrao = 100

jogo1 = Jogador(vida_padrao, aura_padrao, arma_jogador)
inimigo = Inimigo(50, aura_padrao, 'perfurante')

# vai rodar o jogo até um dos personagens ficar com a vida zerada
while jogo1.vida > 0 and inimigo.vida > 0:
    # defino até onde vai o dano e de forma randomizada
    dano_jogador = random.randrange(1, 21)
    dano_inimigo = random.randrange(1, 21)

    jogo1.reduzirVidaInimigo(dano_jogador, arma_jogador, inimigo)
    inimigo.reduzirVidaInimigo(dano_inimigo, 'perfurante', jogo1)

    # mostro as informações do jogador e do inimigo para melhor análise
    jogo1.informacoes()
    print()  # forrmatação para mostrar informações mais organizadamente
    inimigo.informacoes()
    print()  # formatação para mostrar informaçções mais organizadamente


if jogo1.vida <= 0 and inimigo.vida <= 0:
    print('Ambos morreram...')

elif jogo1.vida <= 0:
    print('Você morreu...')

elif inimigo.vida <= 0:
    print('você ganhou...')
