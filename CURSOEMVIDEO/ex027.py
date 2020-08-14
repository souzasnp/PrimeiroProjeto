#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
#Ex: Ana maria de Souza
#Primeiro: ana
#Ultimo Souza
nome = str(input('Digite seu nome completo: ')).strip().upper()
primeironome = nome.split()
print('Seu primeiro nome: {}\n Último sobrenome: {}'.format(primeironome[0], primeironome[len(primeironome)-1]))
