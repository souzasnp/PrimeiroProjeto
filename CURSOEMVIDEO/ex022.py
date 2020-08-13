#Crie um programa que leia o nome completo de uma pessoa e mostre: 
# -  O nome com todas as letras maiusculas
# -  O nome com todas as minusculas
# -  Quantas letras ao todos sem considerar os espaços.
# -  Quantas letras tem o primeiro nome

nome = str(input('Digite o nome completo: '))
espc = nome.replace(" ","")
maius = nome.upper()
minus = nome.lower()
letras = len(espc.strip())
qnt = len(nome.split())
print(maius, minus, letras, qnt)
