#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno cosseno e tangente desse angulo.
import math
angulo = int(input('Informe o angulo: '))
seno = math.sin(angulo)
coss = math.cos(angulo)
tang = math.tan(angulo)
print(' Angulo informado {}º\n Seno: {}\n Cosseno {}\n Tangente {:.2f}'.format(angulo, math.ceil(seno),math.ceil(coss), tang))
