#Crie um programa que leia o nome completo de uma pessoa e mostre: 
# -  O nome com todas as letras maiusculas
# -  O nome com todas as minusculas
# -  Quantas letras ao todos sem considerar os espaços.
# -  Quantas letras tem o primeiro nome

nome = str(input('Digite o nome completo: ')).strip()
espc = nome.replace(" ","")
print('Seu nome em maiúsculo: {}'.format(nome.upper()))
print('Seu nome em minúsculo: {}'.format(nome.lower()))
print('Seu nome tem um total de {} letras.'.format(len(espc)))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))