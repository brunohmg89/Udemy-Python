"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

#Solução 1 com if/else

numero = input('Digite um numero inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = "par"

    print(f'O número "{numero_int}" é um numero inteiro e é {par_impar_texto}')

else:
    
    print('O numero que vc digitou não é inteiro')