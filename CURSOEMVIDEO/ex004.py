n1 = input('ENTRE COM O PRIMEIRO VALOR: ')
print('Qual o tipo primitivo do valor ? {} O valor digitado é : {}.'
      .format(type(n1), n1))
print('O valor digitado é Numérico ? ', n1.isnumeric())
print('O Valor digitado é Alfabético? ', n1.isalpha())
print('O Valor digitado tem espaçamento? ', n1.isspace())
print('O valor digitado é Alfanumérico? ', n1.isalnum())
