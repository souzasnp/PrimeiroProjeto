#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento. -Avista dinheiro/cheque 10% de desconto. -Avista no cartão 5% de desconto. -Em até 2x no cartão preço normal. -3x ou mais no cartão 20% de juros.
print('xxxxxxxxxx PROGRAMA DE DESCONTO xxxxxxxxxx')
valor = float(input('Insira o valor do produto : R$'))
print('Formas de Pagamento:\n 1 - Avista Dinheiro/Cheque 10% de desconto\n 2 - Avista no Cartão 5% de desconto\n 3 - Cartão até 2x Valor normal\n 4 - Cartão 3x ou mais 20% de juros')
cond = int(input('Insira a forma de pagamento: '))
if cond == 1:
    print(' Forma de pagamento escolhida: AVISTA DINHEIRO/CHEQUE\n Valor do produto: R${:.2f}\n Valor produto/desconto: R${:.2f}'.format(valor, valor - (valor * 10 / 100)))
elif cond == 2:
    print(' Forma de pagamento escolhida: AVISTA CARTÃO\n Valor do produto: R${:.2f}\n Valor produto/desconto: R${:.2f}'.format(valor, valor - (valor * 5 / 100)))
elif cond == 3:
    print(' Forma de pagamento escolhida: CARTÃO ATÉ 2X\n Valor do produto: R${:.2f}\n Valor produto/desconto: R${:.2f}'.format(valor, valor ))
elif cond == 4:
    print(' Forma de pagamento escolhida: CARTÃO 3X OU MAIS\n Valor do produto: R${:.2f}\n Valor produto/desconto: R${:.2f}'.format(valor, valor + (valor * 20 / 100)))
print('xxxxxxxxxxxxxxxxxxFIMxxxxxxxxxxxxxxxxxx')