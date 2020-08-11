#Um professor quer sortear um dos seus quatros alunos para apagar o quadro. faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')
resul = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(resul)
print('Aluno escolhido: {}'.format(escolhido))
