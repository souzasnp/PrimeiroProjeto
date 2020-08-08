#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. calcule e mostre o comprimento da hipotenusa.
#
import math
cateoposto = int(input('Digite o comprimento do cateto oposto: '))
cateadjascente = int(input('Digite o comprimento do cateto adjascente: '))
hipotenusa = (cateoposto * cateoposto) + (cateadjascente * cateadjascente)
raiz = math.sqrt (hipotenusa)
print('O Comprimento da Hipotenusa é de : {}'.format(raiz))
