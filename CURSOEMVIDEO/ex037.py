#Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão. 1° binário, 2º octal, 3ºHexadecimal.
from time import sleep
print('xxxxxxxxxxxxxxx Programa de Conversão xxxxxxxxxxxx')
print('Escolha: Binario, Octal, Hexadecimal.')
tipo = str(input('Qual a forma de Conversão: ')).upper()
conv = int(input('Digite um número para conversão: '))
a = bin(conv)[2:]#[2:] fatiamento 
b = oct(conv)[2:]
c = hex(conv)[2:]
print('\033[4;31;40mCarregando...\033[m')
sleep(2)
if tipo == 'BINARIO':
    print('Valor convertido em binário: {}'.format(a))
elif tipo == 'OCTAL':
    print('Valor Convertido em Octal: {}'.format(b))
elif tipo == 'HEXADECIMAL':
    print('Valor Convertido em Hexadecimal: {}'.format(c))
elif tipo != 'BINARIO' and 'OCTAL' and 'HEXADECIMAL':
    print('Tipo de conversão não corresponde, favor tentar novamente!')
print('xxxxxxxxxxxxxxxxxxxxxx FIM xxxxxxxxxxxxxxxxxxxxxx')