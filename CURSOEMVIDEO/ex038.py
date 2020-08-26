#Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem: -O primeiro valor é maior, -O segundo valor é maior, -Não existe valor maior. os dois são iguais.
print('xxxxxxxxxx Comparando  Números xxxxxxxxxx')
a = int(input('Insira o primeiro valor inteiro: '))
b = int(input('insira o segundo valor inteiro: '))
if a > b:
    print('O Primeiro Valor é Maior')
elif b > a:
    print('O Segundo valor é maior')
else:
    print('Não existe valor maior. Os dois são iguais.')
print('xxxxxxxxxxxxxxxxxxxFIMxxxxxxxxxxxxxxxxxxx')