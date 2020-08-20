#Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor.
a= int(input('Insira o primeiro numero: '))
b = int(input('Insira o segundo numero: '))
c = int(input('Insira o terceiro numero:'))
#Analisando menor valor digitado
menor = a
if (b<a) and (b<c):
    menor = b
if (c<a) and (c<b):
    menor = c
#Analisando Maior valor digitado
maior = a
if (b>a) and (b>c):
    maior = b
if (c>a) and (c>b):
    maior = c
print('O maior valor digitado é {}'.format(maior))
print('O menor valor digitado é {}'.format(menor))
