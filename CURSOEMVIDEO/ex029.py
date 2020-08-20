#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado. A multa vai custa R$7,00 por cada km acima do limite.
v = float(input('Entre com a velocidade em Km/h: '))
m = v - 80
if v >= 81:
    print('xxxxxxxxxx LIMITE DE VELOCIDADE 80 KM/H xxxxxxxxxx')
    print('Velocidade Capturada: {} KM/H Valor da Multa: R${:.2f}'.format(v, (m * 7) ))
else:
    print('xxxxxxxxxx LIMITE DE VELOCIDADE 80 KM/H xxxxxxxxxx')
    print('Velocidade Capturada: {} KM/H Você está dentro do limite de velocidade, PARABÉNS.'.format(v))
print('xxxxxxxxxxxxxxxxxxxxFIMxxxxxxxxxxxxxxxxxxxx')
