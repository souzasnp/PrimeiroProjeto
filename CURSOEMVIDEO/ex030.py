#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
n = int(input('Digite um número para descobrir se ele é PAR ou IMPAR: '))
if (n%2) == 0:
    print('O Número digitado {} é PAR.'.format(n))
else:
    print('O Número digitado {} é IMPAR.'.format(n))