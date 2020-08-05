#AulaCursoemVideo - Aula 07: exercicio 011
print('Calculo de Litros de tinta necessário')
larg = float(input('Insira a Largura da parede em metros: '))
alt = float(input('Insira a Altura da parede em metros: '))
area = larg * alt
tinta = area / 2
print(' Largura: {} Metros.\n Altura: {} Metros.\n Total da área: {}m².\n Litros de Tinta necessário: {}L.'
.format(larg, alt, area, tinta))
