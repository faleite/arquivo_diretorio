"""Crie 10 arquivos com o nome ‘live_n.txt’ onde n é o número do arquivo e delete os arquivos
em que o valor é menor ou igual a 5. Quando isso estiver feito, renomeie os arquivos de 6 a 9,
para 1 a 4
"""

import os
import os.path
import shutil
from pathlib import Path

#1 Criando 10 arquivos
for elemento in range(1, 11):
    #  Path('live_{}.txt'.format(elemento)).touch() -> {}.format(value)
    Path(f'live_{elemento}.txt').touch()

# Listar diretórios especificos
# ('.') o ponto representa o diretório atual
#  print([f for f in os.listdir('.') if f.startswith('live_')])
lista = ([f for f in os.listdir('.') if f.startswith('live_')])

#2 Removendo arquivos menores ou iguais a 5
for _file in lista:
    if int(_file.partition('_')[2][0]) <= 5:
        os.remove(_file)


#3 Alterando arquivos restantes
#  print([f for f in os.listdir('.') if f.startswith('live_')])

lista = ([f for f in os.listdir('.') if f.startswith('live_')])

for valor, elemento in enumerate(sorted(lista), start=1):
    shutil.move(elemento, f'live_{valor}.txt')

# print da lista dos arquivos no terminal
lista = ([f for f in os.listdir('.') if f.startswith('live_')])
print(lista)
