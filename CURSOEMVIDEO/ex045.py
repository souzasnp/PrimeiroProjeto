#Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
print('xxxxxxxxxxxxxxx JOKENPO xxxxxxxxxxxxxxx')
print('Escolha entre: PEDRA, PAPEL OU TESOURA')
a = str(input('Jokenpo: ')).lower()
ale = ('pedra', 'papel', 'tesoura')
resul = choice(ale)
if a == resul:
    print(' Empate, tente novamente\n Valor Computador: {}'.format(resul))
elif a == 'pedra' and resul == 'papel':
    print(' O computador Venceu!!!\n Valor Computador: {}'.format(resul))
elif a == 'papel' and resul == 'pedra':
    print(' Você venceu!!!\n Valor Computador: {}'.format(resul))
elif a == 'papel' and resul == 'tesoura':
    print(' O Computador venceu!!!\n Valor Computador: {}'.format(resul))
elif a == 'tesoura' and resul == 'papel':
    print(' Você venceu!!!\n Valor Computador: {}'.format(resul))
elif a == 'tesoura' and resul == 'pedra':
    print(' O Computador venceu!!!\n Valor Computador: {}'.format(resul))
elif a == 'pedra' and resul == 'tesoura':
    print(' Você venceu!!!\n Valor Computador: {}'.format(resul))
elif a != 'pedra' and 'papel' and 'tesoura':
    print('Valor não aceito, escolha entre: PEDRA, PAPEL OU TESOURA!')
print('xxxxxxxxxxxxxxxxx FIM xxxxxxxxxxxxxxxxx')
