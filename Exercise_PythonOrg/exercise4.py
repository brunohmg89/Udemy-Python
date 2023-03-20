'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

nota_bi_1 = input('Digite a note do 1º bimestre: ')
nota_bi_2 = input('Digite a note do 2º bimestre: ')
nota_bi_3 = input('Digite a note do 3º bimestre: ')
nota_bi_4 = input('Digite a note do 4º bimestre: ')

nota_bi_1 = float(nota_bi_1)
nota_bi_2 = float(nota_bi_2)
nota_bi_3 = float(nota_bi_3)
nota_bi_4 = float(nota_bi_4)

media = (nota_bi_1 + nota_bi_2 + nota_bi_3 + nota_bi_4) / 4

print (f'Sua média foi de {media:.1f}')