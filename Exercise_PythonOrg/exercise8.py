'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

valor_hora = input('Digite quanto você ganha por hora: ')
valor_hora_float = float(valor_hora)

horas_trabalhadas = input('Digite quantas horas você trabalhou esse mês: ')
horas_trabalhadas_float = float(horas_trabalhadas)

total_valor_hrs_trabalhadas = horas_trabalhadas_float * valor_hora_float

print(f'Você ganhou {total_valor_hrs_trabalhadas} esse mês')


