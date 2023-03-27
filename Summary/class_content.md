# Iniciando as aulas

## Seção 1: Informações e avisos importantes + Boas vindas

## Seção 2: Python + VS Code: Preparando o ambiente

- Configuração do VSCode e dicas

## Seção 3: Iniciando programação com Python    

- aula1.py - Comentários ```#``` e DockString ```"""```

- aula2.py - Separadores

- aula3.py - Python uma linguagem de tipagem **FORTE** & **DINAMICA**

- aula4.py - Tipos de váriavel - **FLOAT** - Ponto Flutuante = *1.2*

- aula5.py - Tipos de váriavel - **BOOL** Booleano - *TRUE* ou *FALSE*

- aula6.py - Conversão de tipos de váriavel, coerção

- aula7.py - Utilizando as váriaveis, mostrando "**nome**" (*string*) e se é maior de idade (*Booleano*)

- aula8.py - Utilizando as váriaveis, mostrando todos os tipos de váriaveis (*string, inteiro, booleano e 
ponto flutuante*)

- aula9.py - Operações aritméticas (**soma (*+*), subtração (*-*), divisão (*/*), multiplicação (*), divisão inteira (*//*), exponenciação *(****) e resto de divisão (**%))

- aula10.py - Concatenação (Operações aritméticas utilizando Strings)

- aula11.py - Operações aritiméticas são realizadas de dentro para fora e primeiro as operações que estão dentro dos parenteses.

- aula12.py - Utilizando operação aritmética para calcular IMC de uma pessoa.

- aula13.py - Formatação de texto com ```f-strings```, utilizando váriaveis dentro de chaves (**{}**) e setar quantidades de números após a vírgula (**:.2f**).

- aula14.py - Formatação de texto com a função ```string.format```

- aula15.py - Criando *entrada* de um valor digitado pelo usuário utilizando ```input``` e realizando uma operação aritmética.

- aula16.py - Condição com ```if / elif / else``` (se / se não se / se não)

- aula17.py - Exemplo de condição ```if / elif / else``` com *TRUE* e *FALSE*

- aula18.py - Outro exemplo de condição ```if / elif / else``` com *TRUE* e *FALSE*

- aula19.py - Operadores de comparação: **Maior** (>), **Maior ou igual** (>=), **Menor** (<), **Menor ou igual** (<=), **Igual** (=) e **Diferente** (!=)

- aula20.py - Exercicio utilizando operadores de comparação.

- aula21.py - Operadores lógicos **AND**, **OR** e **NOT**
    - **AND** - Todas as condições precisam ser verdadeiras se qualquer valor for considerado falso a expressão inteira será avaliada naquele valor.
    - São considerados valores *falsos*: 0 - 0.0 - '' - False
    - Valor **NONE** para representar um *não* valor.

- aula22.py - Operadores lógicos **AND**, **OR** e **NOT**
    - **OR** - Qualquer condição verdadeira avalia toda a expressão como verdadeira. Se qualquer valor for considerado verdadeiro a expressão inteira será avaliada naquele valor.

- aula23.py - Operadores lógicos **AND**, **OR** e **NOT**
    - **NOT** Utilizada para inverter expressões de *TRUE* para *FALSE* ou de *FALSE* para *TRUE*

- aula24.py - Operador **in** e **not in**

- aula25.py - Interpolação básica de Strings utilizando sinal de %.

- aula26.py - Formatação básica de string utilizando os sinais **(> < ^ = - +)**

- aula27.py - Fatiamento de strings utilizando **[i:f:p]** após a utilização da váriavel, visto também a função *len* que retorna a quantidade de carecteres de uma string.

- aula28.py - Exercicios utilizando o fatiamento de strings

- aula29.py - Introdução ao **TRY/EXCEPT**
    - **Try** Tentar executar o código
    - **Except** Tratamente de erros/exceções.

- aula30.py - Exemplo de váriaveis "constantes" que não irão alterar.

- aula31.py - Adicionando Flag (bandeira), nada mais é do que marcar um local no código. Váriavel None = Não valor. Operadores **is** e **is not** (é ou não é).

- aula32.py - Exercicios
    - Exercicio para informar se um número digitado é inteiro e se ele é par ou impar.
    - Exercicio para saudar com *bom dia*, *boa tarde* ou *boa noite* dependendo da hora (número inteiro) que for digitado.
    - Exercicio para tratar a quantidade de letras de um nome que for digitado e mostrar se ele é pequeno, normal ou grande.

- aula33.py - Revendo tipos de váriaveis imutaveis que vimos (str, int, float, bool) e função *.zfill.

- aula34.py - 

- aula39_exercise_s1 - aula39_exercise_s2:
    - Exercicio: Iterando strings com while

- aula40_exercise.py:
    - Exercicio: Calculadora com while

- aula41.py:
    - while / else

- aula42_p1 - aula42_p2 - aula43_p1 - aula43_p2:
    - While simples
    - Iteração

- aula44.py:
    - For + Range
    - range -> range(start, stop, step)

- aula45.py - aula46.py:
    - Iterável -> str, range, etc (__iter__)
    - Iterador -> quem sabe entregar um valor por vez
    - next -> me entregue o próximo valor
    - iter -> me entregue seu iterador


- aula47_exercise_s1 - aula47_exercise_s2 - aula47_exercise_s3:
    - Exercicio: 
        - Faça um jogo para o usuário adivinhar qual a palavra secreta.
        - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
        - Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
        - Se a letra digitada estiver na palavra secreta, exiba a letra,
        - Se a letra digitada não estiver na palavra secreta, exiba *.
        - Faça a contagem de tentativas do seu usuário.

- aula48.py - aula49.py - aula50.py - aula51.py:
    - Listas em Python
        - Tipo list - Mutável
        - Suporta vários valores de qualquer tipo
        - Conhecimentos reutilizáveis - índices e fatiamento
        - Métodos úteis:
            - append - Adiciona um item ao final
            - insert - Adiciona um item no índice escolhido
            - pop - Remove do final ou do índice escolhido
            - del - apaga um índice
            - clear - limpa a lista
            - extend - estende a lista
            - (+) - concatena listas
            - CRUD = Create Read Update Delete
            
            ```
                C      R    U        D        (CRUD)
                Create Read Update   Delete
                Criar  ler  alterar  apagar = lista[i]
            ```

- aula52.py:
    - Cuidados com dados mutáveis
    - = copiado o valor (imutáveis)
    - = aponta para o mesmo valor na memória (mutável)

- aula53.py:
    - for in com listas

- aula54.py:
    - Exercício
        - Exiba os índices da lista
        - 0 Maria
        - 1 Helena
        - 2 Luiz

- aula55.py:
    - Introdução ao empacotamento e desempacotamento

- aula56.py:
    - Tipo tupla - Uma lista imutável

- aula57.py:
    - enumerate - enumera iteráveis (índices)

- aula58_exercise_s1 - aula58_exercise_s2:
    - Faça uma lista de comprar com listas
        - O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
        - Não permita que o programa quebre com erros de índices inexistentes na lista.

- aula59.py:
    - Imprecisão de ponto flutuante
    - Double-precision floating-point format IEEE 754 <https://en.wikipedia.org/wiki/Double-precision_floating-point_format> 
    - <https://docs.python.org/pt-br/3/tutorial/floatingpoint.html>

- aula60.py:
    - split e join com list e str
        - **split**: Divide uma string (retorna uma lista)
        - **join**: Une uma string

- aula61.py:
    - Lista dentro de lista, acessando os dados com for.

- aula62.py:
    - Detalhes sobre o interpretador do Python.

- aula63.py:
    - Desempacotamento em chamadas de métodos e funções.

- aula64.py:
    - Operação ternária em Python
        - if e else de uma linha
        - (valor) if (condicao) else (outro valor)

- aula65_exercise_s1.py - aula65_exercise_s2 - aula65_exercise_s3 - aula65_exercise_s4:
    - Exercicio - Calculo do primeiro digito do CPF
        - CPF:
        ```
            746.824.890-70
        ```
        - Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 10:
        ```
            10   9  8  7  6  5  4  3  2
         *   7   4  6  8  2  4  8  9  0
            70  36 48 56 12 20 32 27  0
        ```
        - Somar todos os resultados: 
        ``` 
            70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301
        ```
        - Multiplicar o resultado anterior por 10:
        ```
            301 * 10 = 3010
        ```
        - Obter o resto da divisão da conta anterior por 11:
        ```
            3010 % 11 = 7
        ```
        - Se o resultado anterior for maior que 9:
            - resultado é 0
        contrário disso:
            - resultado é o valor da conta
        - O primeiro dígito do CPF é 7

    - Exercicio - Calculo do primeiro segundo digito do CPF:
        - CPF:
        ```
            746.824.890-70
        ```
        - Colete a soma dos 9 primeiros dígitos do CPF, Mais o primeiro digito, multiplicando cada um dos valores por uma contagem regressiva começando de 11:
        ```
            11  10  9  8  7  6  5  4  3  2
         *   7   4  6  8  2  4  8  9  0  7
            77  40 54 64 14 24 40 36  0 14
        ```
        - Somar todos os resultados: 
        ``` 
            77 + 40 + 54 + 64 + 14 + 24 + 40 + 36 + 0 + 14 = 363
        ```
        - Multiplicar o resultado anterior por 10:
        ```
            363 * 10 = 3630
        ```
        - Obter o resto da divisão da conta anterior por 11:
        ```
            3630 % 11 = 0
        ```
        - Se o resultado anterior for maior que 9:
            - resultado é 0
        contrário disso:
            - resultado é o valor da conta
        - O segundo dígito do CPF é 0

- aula65_exercise_s5
    - Exercio - Gerando CPFs aleatórios verdadeiros com base no calculo e de CPF feito no exercicio anterior.


## Seção 4: Python intermediário - Funções, dicionários, módulos, Programação Funcional e +

- aula66.py:
    - Introdução às funções (def) em Python.
        - Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
        - Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
        - Por padrão, funções Python retornam None (nada).

- aula67.py: 
    - Argumentos nomeados e não nomeados em funções Python.
        - Argumento nomeado tem nome com sinal de igual
        - Argumento não nomeado recebe apenas o argumento (valor).

- aula68.py:
    - Valores padrão para parâmetros.
        - Ao definir uma função, os parâmetros podem ter valores padrão
        - Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
        - Refatorar - Editar o seu código.

- aula69_p1.py:
    - Escopo de funções em Python.
        - Escopo significa o local onde aquele código pode atingir.
        - Existe o escopo global e local.
        - O escopo global é o escopo onde todo o código é alcançavel.
        - O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.

- aula69_p2.py:
    - Não temos acesso a nomes de escopos internos nos escopos externos.
    - A palavra global faz uma variável do escopo externo ser a mesma no escopo interno.

- aula70.py:
    - Retorno de valores das funções **return**

- aula71.py:
    - args - Argumentos não nomeados 
    - *args - empacotamento e desempacotamento

- aula72_exercise.py:
    - Exercícios com funções:
        - Crie uma função que multiplica todos os argumentos não nomeados recebidos e retorne o total para uma variável e mostre o valor da variável.

- aula73.py:
    - Higher Order Functions
    - Funções de primeira classe

- aula74.py:
    - Closure e funções que retornam outras funções

- aula75_exercise_s1.py:
    - Exercícios (repetindo código)
    - Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.

- aula75_exersice_s2.py:
    - Exercícios (criando um multiplicador com argumento)
    - Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.

- aula76.py:
    - Dicionários em Python (tipo dict)
        - Dicionários são estruturas de dados do tipo par de "chave" e "valor". Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc. O valor pode ser de qualquer tipo, incluindo outro dicionário. Usamos as chaves - {} - ou a classe dict para criar dicionários.
        - Imutáveis: str, int, float, bool, tuple
        - Mutável: dict, list

- aula77.py:
    - Manipulando chaves e valores em dicionários

- aula78.py e aula79.py:
    - Métodos úteis dos dicionários em Python:
        - len - quantas chaves
        - keys - iterável com as chaves
        - values - iterável com os valores
        - items - iterável com chaves e valores
        - setdefault - adiciona valor se a chave não existe
        - copy - retorna uma cópia rasa (shallow copy)
        - get - obtém uma chave
        - pop - Apaga um item com a chave especificada (del)
        - popitem - Apaga o último item adicionado
        - update - Atualiza um dicionário com outro