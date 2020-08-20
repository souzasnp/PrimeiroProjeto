nome = input('Digite seu nome: ')
cores = {'limpa':'\033[m', 'azul' : '\033[34m'}
print('É um prazer te conhecer, {}{}{}!'.format(cores['azul'],nome,cores['limpa']))
