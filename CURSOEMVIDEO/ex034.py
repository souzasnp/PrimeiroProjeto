#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para Salários superiores a R$1250,00 calcule um aumento de 10%. Para inferiores ou iguais o aumento é de 15%.
salario = float(input('Informe o salário do funcionário: R$'))
if salario => 1250:
    print('Salário atual: R${} Salário com aumento: R${}'.format(salario ))