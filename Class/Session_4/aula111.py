from sys import path

import aula111_package.modulo
from aula111_package import modulo
from aula111_package.modulo import *

# from aula111_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula111_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)