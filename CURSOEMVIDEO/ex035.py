#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('xxxxxxxxxTipos de TRIANGULOxxxxxxxxxx')
a = int(input('Digite o valor da 1º reta: '))
b = int(input('Digite o valor da 2º reta: '))
c = int(input('Digite o valor da 3º reta: '))
if (a + b < c) or (a + c < b) or (b + c < c):
    print('Não é um TRIANGULO')
elif (a == b) and (a == c) :
        print('Equilatero')
elif (a==b) or (a==c) or (b==c):
        print('Isósceles')
else:
        print('Escaleno')
print('xxxxxxxxxxxxxxxFIMxxxxxxxxxxxxxxx')