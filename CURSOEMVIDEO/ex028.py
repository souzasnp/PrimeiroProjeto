#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
n = int(input(' entre com o número: '))
a = randint(0,5) #gera números aleatórios
print('PROCESSANDO...')
sleep(3) #faz o computador dormir.
if n == a:
    print('VOCÊ VENCEU!!! O NÚMERO SORTEADO É : {}'.format(a))
else:
    print('VOCÊ PERDEU!!! O NÚMERO SORTEADO FOI {}'.format(a))
print('xxxxxxxxxxxxxxxxxxxFIMxxxxxxxxxxxxxxxxxxxxx')
