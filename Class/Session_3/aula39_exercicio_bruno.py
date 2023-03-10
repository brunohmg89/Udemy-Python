"""
Iterando strings com while
"""
   
nome = 'Bruno Henrique'  # Iteráveis

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)

#nova_string = ''
#nova_string += '*B*r*u*n*o*H*e*n*r*i*q*u*e*'

