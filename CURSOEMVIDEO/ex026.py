# Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A" - Em que posição ela aparece a primeira vez - Em que posição ela aparece a última vez.
frase = str(input('Digite a frase: '))
maius = frase.upper()
n1 = maius.count('A')
n2 = maius.find('A')
print(n1,n2)