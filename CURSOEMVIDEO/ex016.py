#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#ex : Digite um número : 6.127 tem a parte inteira 6
#Dica: olhar todas a funções dentro da biblioteca math.
from math import trunc
real = float(input('Digite um número: '))
resul = trunc(real)
print('A parte inteira de {} é {}'.format(real, resul))
