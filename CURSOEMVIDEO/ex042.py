#Refaça o Desafio 035 dos Triangulos acrescentando o recurso de mostrar que tipo de triangulo será formado: -Equilatero todos os lados iguais, -Isosceles dois lados iguais, -Escaleano todos os lados diferentes.
from time import sleep
print('xxxxxxxxxx TIPOS DE TRIANGULOS xxxxxxxxxx')
a = float(input('Digite o valor da 1º reta: '))
b = float(input('Digite o valor da 2º reta: '))
c = float(input('Digite o valor da 3º reta: '))
print('\033[1;31;40m[Carregando...]\033[m')
sleep(2)
if (a==b) and (a==c):
    print('EQUILATERO')
elif (a==b) or (a==c) or (b==c):
    print('ISOSCELES')
else:
    print('ESCALEANO')
print('xxxxxxxxxxxxxxxxxx FIM xxxxxxxxxxxxxxxxxx')