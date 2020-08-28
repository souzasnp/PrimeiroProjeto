#Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo. -Abaixo de 18.5: abaixo do peso, -Entre 18.5 e 25: Peso ideal, -25 até 30: sobrepeso, -30 até 40: obesidade, acima de 40: obesidade mórbida.
from time import sleep
print('xxxxxxxxxxx CALCULO IMC xxxxxxxxxxx')
peso = float(input('Insira o seu peso: '))
altura = float(input('Insira sua altura: '))
r = peso / (altura * 2)
print('\033[1;33;40m[CALCULANDO...]\033[m')
sleep(2)
if r <= 18.4:
    print('Você está abaixo do \033[1;31;40mPESO!\033[m PROCURE UM MÉDICO!')
elif r <= 25:
    print('Você está com peso \033[1;34;40mIDEAL!\033[m Excelente!')
elif r <= 30:
    print('Você está com \033[1;33;40mSOBREPESO!\033[m Cuide-se!')
elif r <= 40:
    print('Você está com \033[1;31;40mOBESIDADE!\033[m PROCURE UM MÉDICO!')
else:
    print('Você está com \033[4;31;40mOBESIDADE MÓRBIDA!\033[m PROCURE UM MÉDICO URGENTEMENTE!')
print('xxxxxxxxxxxxxxx FIM xxxxxxxxxxxxxxx')