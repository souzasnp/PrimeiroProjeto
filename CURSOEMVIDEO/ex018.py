#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno cosseno e tangente desse angulo.
import math
angulo = int(input('Informe o angulo: '))
seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print(' Angulo informado {}º\n Seno: {:.2f}\n Cosseno {:.2f}\n Tangente {:.2f}'.format(angulo, seno, coss, tang))
