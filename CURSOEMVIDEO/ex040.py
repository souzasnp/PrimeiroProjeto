#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida. -Média abaixo de 5.0 Reprovado. -Média entre 5.0 e 6.9 Recuperação. -Média 7.0 acima ou superior Aprovado.
print('xxxxxxxxxx Calculo Média Aluno xxxxxxxxxx')
m1 = float(input('Insira a 1º nota do aluno: '))
m2 = float(input('Insira a 2º nota do aluno: '))
media = (m1 + m2) / 2
print('A média do aluno é : {:.1f}'.format(media))
if media < 5:
    print('REPROVADO')
elif media >= 7:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')
print('xxxxxxxxxxxxxxxxxxxFIMxxxxxxxxxxxxxxxxxxx')