#Escreva um programa para aprova o empréstimo bancário para a compra de uma casa. O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
print('xxxxxxxxxxx Programa de Empréstimo xxxxxxxxxxx')
vcasa = float(input('Informe o valor do imóvel: R$'))
salario = float(input('Qual o salário do Comprador: R$'))
tempo = int(input('Insira o periodo de financiamento em meses: '))
parcela = vcasa / tempo
if parcela > salario * 30 / 100:
    print('Sua solicitação de empréstimo foi NEGADA')
else:
    print('Sua solicitação de empréstimo foi APROVADA')
    print(' Valor do imovel: R${:.2f}\n Valor Mensal das Prestações: R${:.2f}\n Número de parcelas: {} meses '.format(vcasa, parcela, tempo))
print('xxxxxxxxxxxxxxxxxxxxxxFIMxxxxxxxxxxxxxxxxxxxxxx')