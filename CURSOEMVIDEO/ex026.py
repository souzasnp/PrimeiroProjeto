# Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A" - Em que posição ela aparece a primeira vez - Em que posição ela aparece a última vez.
frase = str(input('Digite a frase: '))
maius = frase.upper()
n1 = maius.count('A')
n2 = maius.find('A')
n3 = maius.rfind('A')
print(' Vezes em que aparece a letra "A": {}\n Qual o valor da sua primeira posição: {}\n Qual o Valor da sua ultima posição: {}'.format(n1,n2, n3))
