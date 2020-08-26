#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: -Se ele ainda vai se alistar ao serviço militar. -Se é a hora de se alistar.-Se já passou o tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Informe o ano de nascimento: '))
r = date.today().year - ano
if r <= 17:
    print('Infelizmente você não poderá se alistar, ESPERA SEU PERIODO DE ALISTAMENTO CHEGAR.')
    print('Tempo que falta para se alistar: {}')
elif r == 18:
    print('Seu periodo de ALISTAMENTO chegou, acesse o site: https://www.alistamento.eb.mil.br/')
else:
    print('Infelizmente seu tempo de se alistar já se esgotou, ')
print('TENHA UM EXCELENTE DIA!!!!')
print(r)