#AulaCursoemVideo - Aula 07: exercicio 010
print('=====Conversor de R$/U$=====')
reais = float(input('Insira o valor em Carteira R$: '))
#3.27 é a cotação do dolár no dia escolhido
dolar = reais / 3.27
print('Você possui R${:.2f}, Podendo comprar U${:.2f}'.format(reais, dolar))
