#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
from random import shuffle
aluno1 = str(input('Primeiro Aluno: '))
aluno2 = str(input('Segundo Aluno: '))
aluno3 = str(input('Terceiro Aluno: '))
aluno4 = str(input('Quarto Aluno: '))
resul = [aluno1, aluno2, aluno3, aluno4]
shuffle(resul)
print('Ordem de Apresentação:')
print(resul)
