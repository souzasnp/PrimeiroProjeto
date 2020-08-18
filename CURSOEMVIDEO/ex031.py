#Desenvolva um programa que pergunte a distancia de uma viagem em km. calcule o preço da passagem, cobrando R$0.50 por km para viagens até 200 km e R$0.45 para viagens mais longas.
print('xxxxxxxxxxxxCÁLCULO DE VIAGEMxxxxxxxxxxxx')
km = float(input('Informe a distância a ser percorrida: '))
if km <= 200:
    print('Sua viagem custará: R$ {:.2f}'.format(km * 0.50))
else:
    print('Sua viagem custará: R$ {:.2f}'.format(km * 0.45))
print('xxxxxxxxxxxxxxxxxxxFIMxxxxxxxxxxxxxxxxxxx')