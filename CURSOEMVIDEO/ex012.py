print('=====Calculo de Descontos=====')
prod = float(input(' Insira o valor do produto: R$ '))
desc= 5
resul = prod - (prod * desc / 100) 
print(' Valor do Produto: R${:.2f}\n Desconto: {}%\n Valor Produto/Desconto: R${:.2f}'.format(prod, desc, resul ))
