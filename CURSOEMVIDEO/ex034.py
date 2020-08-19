#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para Salários superiores a R$1250,00 calcule um aumento de 10%. Para inferiores ou iguais o aumento é de 15%.
print('xxxxxxxxxxPrograma Aumento de Salárioxxxxxxxxxx')
salario = float(input(' Informe o salário do funcionário: R$'))
dez = salario + (salario * 10 /100)
quinze = salario + (salario * 15 /100)
if salario >= 1251:
    print(' Salário atual: R${:.2f} Salário com aumento: R${:.2f}'.format(salario, dez))
else:
    print(' Salario atual: R${:.2f} Salário com aumento: R${:.2f}'.format(salario, quinze))
print('xxxxxxxxxxxxxxxxxxxxxxFIMxxxxxxxxxxxxxxxxxxxxxxx')
