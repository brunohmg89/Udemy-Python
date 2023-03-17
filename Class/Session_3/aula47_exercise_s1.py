"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
letras = input('Digite uma letra: ')
palavra_secreta = 'perfume'

for letra in palavra_secreta:

    if letra == 'p':
        print(letra)

    elif letra == 'e':
        print(letra)

    elif letra == 'r':
        print(letra)

    elif letra == 'f':
        print(letra)

    elif letra == 'u':
        print(letra)

    elif letra == 'm':
        print(letra)

    else:
        print('*')