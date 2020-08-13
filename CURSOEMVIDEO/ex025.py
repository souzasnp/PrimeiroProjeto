# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input('Digite o nome completo: '))
maius = nome.upper()
resul = maius.find('SILVA')
print(resul)
