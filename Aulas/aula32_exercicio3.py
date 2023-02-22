"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
numero_qtd_letras = len(nome)

if numero_qtd_letras > 1:
    if numero_qtd_letras <= 4:
        print(f'Seu nome é muito curto')

    elif numero_qtd_letras >= 5 and numero_qtd_letras <=6:
        print(f'Seu nome é normal')

    else:
         print(f'Seu nome é muito grande')

else:
    print('Digite mais de 1 letra')