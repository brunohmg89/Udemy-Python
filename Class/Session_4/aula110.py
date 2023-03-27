import importlib

import aula110_module

print(aula110_module.variavel)

for i in range(10):
    importlib.reload(aula110_module)
    print(i)

print('Fim')