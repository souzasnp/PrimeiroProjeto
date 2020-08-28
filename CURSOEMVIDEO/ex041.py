#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade: -Até 9 anos MIRIM. -Até 14 anos INFANTIL. -Até 19 anos JUNIOR. -Até 20 anos SENIOR.-Acima MASTER.
from datetime import date
from time import sleep
print('xxxxxxxxxx Conf. Nacional de Natação xxxxxxxxxx')
ano = int(input('Insira o ano do nascimento do atleta: '))
data = date.today().year - ano
print('\033[7;31;40mPROCESSANDO...\033[m')
sleep(3) #faz o computador dormir.
if data <= 9:
    print(' Idade: {} anos\n Perfil: Natação \033[1;34;40mMIRIM!\033[m'.format(data))
elif data <= 14:
    print(' Idade: {} anos\n Pefil: Natação \033[1;34;40mINFANTIL!\033[m'.format(data))
elif data <= 19:
    print(' Idade: {} anos\n Pefil: Natação \033[1;34;40mJUNIOR!\033[m'.format(data))
elif data == 20:
    print(' Idade: {} anos\n Pefil: Natação \033[1;34;40mSENIOR!\033[m'.format(data))
else:
    print(' Idade: {} anos\n Pefil: Natação \033[1;34;40mMASTER!\033[m'.format(data))
print('xxxxxxxxxxxxxxxxxxxxxxxFIMxxxxxxxxxxxxxxxxxxxxxx')