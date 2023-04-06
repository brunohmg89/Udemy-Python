import json

pessoa = {
    'nome': 'Bruno Henrique',
    'sobrenome': 'Maia',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('C:\\Users\\Bruno\\Desktop\\GitHub\\Curso-Python\\Class\\Session_4\\aula135_arquivo\\aula136.json',
           'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

with open('C:\\Users\\Bruno\\Desktop\\GitHub\\Curso-Python\\Class\\Session_4\\aula135_arquivo\\aula136.json',
          'r', encoding='utf8') as arquivo:
   pessoa = json.load(arquivo)
   # print(pessoa)
   # print(type(pessoa))
   print(pessoa['nome'])