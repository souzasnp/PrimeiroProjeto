# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
cidade = str(input('Digite o nome da cidade: ')).strip()
resul = cidade.upper()
print('O nome da sua cidade começa com SANTO: {}'.format(resul[:5] == 'SANTO'))
