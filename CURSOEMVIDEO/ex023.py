# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. ex: Digite um número: 1834 
# unidade: 4 Dezena: 3 Centena: 8 milhar: 1

numero = input('Digite um número de 0 a 9999: ')
print(' Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}'.format(numero[3], numero[2], numero[1], numero[0]))