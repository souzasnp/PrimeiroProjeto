# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. ex: Digite um número: 1834 
# unidade: 4 Dezena: 3 Centena: 8 milhar: 1

numero = int(input('Digite um número de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(' Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}'.format(u, d, c, m))
