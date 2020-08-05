print('=====Calculo de Aumento de Salário=====')
salario = float(input('Entre com o valor do salário Atual: R$'))
porc = float(input('Qual o valor em (%) de aumento:  '))
calc = salario * porc / 100
resul = salario + calc
print(' Salário informado: R${:.2f}\n Porcentagem de aumento: {}%\n Salário com aumento: R$ {:.2f}'.format(salario, porc, resul))
