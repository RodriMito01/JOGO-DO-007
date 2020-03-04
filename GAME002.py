from random import randint
from time import sleep
from os import system


def cls():
    system('cls')


def leiaint(msg:str):
    while True:
        try:
            n = int(input(msg))
            if n <= 2 and n >= 0:
                return n
            else:
                pass
        except ValueError:
            print('SOMENTE DIGITE 0, 1 OU 2')
        except KeyboardInterrupt:
            pass
        except Exception as e:
            pass

try:
    itens = ('DEFESA', 'ATAQUE', 'CARREGAR')
    bot = 0
    jog = 0
    Bot = 2
    print('---Jogo DO 007!---')
    while True:
        print('''Suas jogadas são:
        [0] DEFESA
        [1] ATAQUE
        [2] CARREGAR''')
        Player = leiaint('Qual a sua jogada: ')
        cls()
        print('0')
        sleep(1)
        cls()
        print('00')
        sleep(1)
        cls()
        print('007!!!!')
        sleep(1)
        cls()
        print('=-=-' * 10)
        print('O jogador escolheu: {}'.format(itens[Player]))
        print('Bot escolheu: {}'.format(itens[Bot]))
        print('=-=-' * 10)
        print(f'bot: {bot} jog:{jog}')
        sleep(2)
        if Bot == 0:  # DEFESA
            if Player == 0:
                print('AMBOS DEFENDEM')
            elif Player == 1:
                jog -= 1
                print('JOGO CONTINUA')
            elif Player == 2:
                jog += 1
                print('BOT SALVO')
            else:
                print('JOGADA INVÁLIDA')
        elif Bot == 1:  # ATAQUE
            if Player == 0:
                bot -= 1
                print('JOGO CONTINUA')
            elif Player == 1:
                bot -= 1
                jog -= 1
                print('JOGO CONTINUA')
            elif Player == 2:
                if bot > 0:
                    bot -= 1
                    print('BOT VENCE')
                    break
                else:
                    print('NÃO SE ATIRA SEM BALA, BOT!')
            else:
                print('JOGADA INVÁLIDA')
        elif Bot == 2:  # CARREGAR
            if Player == 0:
                bot += 1
                print('JOGO CONTINUA')
            elif Player == 1:
                if jog > 0:
                    jog -= 1
                    print('PLAYER VENCE')
                    break
                else:
                    print('NÃO SE ATIRA SEM BALA, JOGADOR!')
            elif Player == 2:
                bot += 1
                jog += 1
            else:
                print('JOGADA INVÁLIDA')
        Bot = randint(0, 2)
except KeyboardInterrupt:
    print('O Jogador interrompeu o processo com Ctrl+C!\nVolte Sempre!')
