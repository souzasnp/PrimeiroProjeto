print('=====Calculo de Descontos=====')
prod = float(input(' Insira o valor do produto R$: '))
desc= 0.05
resul = prod - (prod * desc) 
print(' Valor do Produto: R${:.2f}\n Desconto: {}%\n Valor Produto/Desconto: R${:.2f}'.format(prod, desc*100, resul ))
