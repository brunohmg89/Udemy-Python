"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = [ ]

while True:
    print('Selecione uma das opções a seguir')
    opcao = input('[i]inserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        produto = input('Insira seu produto: ')
        lista.append(produto)

        print(f'Inserindo {produto} na lista')

    elif opcao == 'a':
        indice_str = input('Digite o indice que será apagado: ')
        print(f'O indice apagado foi {indice_str}')

        try:
            indice_num = int(indice_str)
            del lista[indice_num]
        except ValueError:
            print('Digite um numero inteiro!')
        except IndexError:
            print('Indice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('Nenhum item para listar')

        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print('Digite uma opção correta')
