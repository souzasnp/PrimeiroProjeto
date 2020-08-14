# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input('Digite o nome completo: ')).strip()
print('Exite SILVA no seu nome: {}'.format('SILVA' in nome.upper()))
