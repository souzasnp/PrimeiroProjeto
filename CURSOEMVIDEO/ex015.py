km = float(input('Informe a quantidade de Km rodado: '))
dias = int(input('Quantidade de dias alugado: '))
soma = (km * 0.15) + (dias * 60)
print('O valor a ser pago é de R$ {:.2f}'.format(soma))
