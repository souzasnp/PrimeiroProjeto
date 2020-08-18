#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
print('xxxxxxxxxxBISSEXTOxxxxxxxxxx')
ano = int(input('Informe o ano que deseja verificar se é bissexto: '))
if (ano%4)==0:
    print('O ano de {} é BISSEXTO.'.format(ano))
else:
    print('O ano de {} não é BISSEXTO.'.format(ano))
print('xxxxxxxxxxxxFIMxxxxxxxxxxxx')