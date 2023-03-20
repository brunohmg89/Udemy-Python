'''
Faça um Programa que converta metros para centímetros.
'''

valor_em_metros = input('Digite um valor em metros para conversão em centímetros: ')
valor_em_metros_float = float(valor_em_metros)

valor_em_centimetros = valor_em_metros_float * 100

print(f'{valor_em_metros} metros fica {valor_em_centimetros:.0f} em centímetros')