print('---Jogo DO 007!---')
from random import randint
from time import sleep


itens = ('DEFESA', 'ATAQUE', 'CARREGAR')
bot = 0
jog = 0
while True:
    Bot = randint(0, 2)
    print('''Suas jogadas são:
    [0] DEFESA
    [1] ATAQUE
    [2] CARREGAR''')
    Player = int(input('Qual sua jogada: '))
    print('0')
    sleep(1)
    print('0')
    sleep(1)
    print('7!!!!')
    print('=-=-' * 10)
    print('O jogador escolheu: {}'.format(itens[Player]))
    print('Bot escolheu: {}'.format(itens[Bot]))
    print('=-=-' * 10)
    sleep(2)
    if Bot == 0:  # DEFESA
        if Player == 0:
            print('AMBOS DEFENDEM')
        elif Player == 1:
            print('JOGO CONTINUA')
        elif Player == 2:
            print('BOT SALVO')
        else:
            print('JOGADA INVÁLIDA')
    elif Bot == 1:  # ATAQUE
        if Player == 0:
            print('JOGO CONTINUA')
        elif Player == 1:
            print('JOGO CONTINUA')
        elif Player == 2:
            print('BOT VENCE')
        else:
            print('JOGADA INVÁLIDA')
    elif Bot == 2:  # CARREGAR
        if Player == 0:
            print('JOGO CONTINUA')
        elif Player == 1:
            print('PLAYER VENCE')
        elif Player == 2:
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA')
