# Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A" - Em que posição ela aparece a primeira vez - Em que posição ela aparece a última vez.
frase = str(input('Digite a frase: ')).strip().upper()
n1 = frase.count('A')
n2 = frase.find('A')+1
n3 = frase.rfind('A')+1
print(' Vezes em que aparece a letra "A": {}\n Qual o valor da sua primeira posição: {}\n Qual o Valor da sua ultima posição: {}'.format(n1,n2,n3))
