""" Criar um diretório ‘aulinha_1’, caso ele não exista, e criar um arquivo chamado ‘xpto.txt’,
se o arquivo já existir, vamos remover e usar o novo. A partir do ‘xpto.txt’
vamos copiar esse arquivo em outros 3 arquivos (‘xpto_1.txt’, ‘xpto_2.txt’ e ‘xpto_3.txt’).
Ao final, vamos listar o diretório e fazer uma assertiva de que nesse diretório só existem
4 arquivos.
"""

import os
import os.path
import shutil
from pathlib import Path

# Criar path caso ele não exista
if not os.path.exists('aulinha_1'):
    os.mkdir('aulinha_1')
#  else:
    #  print('Diretório já existe')

# Definir diretório a estar
os.chdir('aulinha_1')

#3 - Maneira de criar arquivo com o pathlib
#  Path('aulinha_1/xpto.txt').touch()
# Com o uso so os.chdir, elimina necessidade de passar o diretório
Path('xpto.txt').touch()

#2 - Maneira de criar arquivo
#  with open('aulinha_1/xpto.txt', 'w') as file:
    #  file.write('')

#1 - Maneira de criar arquivo
#  file = open('aulinha_1/xpto.txt', 'w')
#  file.write('')
#  file.close()


#  shutil.copy('xpto.txt', 'xpto_1.txt')
#  shutil.copy('xpto.txt', 'xpto_2.txt')
#  shutil.copy('xpto.txt', 'xpto_3.txt')
for elemento in range(1, 4):
    shutil.copy('xpto.txt', f'xpto_{elemento}.txt')


# Mostra o caminho do diretório atual
#  print(os.getcwd())

#  arquivos_aula = os.listdir('.')
#  print(arquivos_aula)

# Assertiva para saber se só existem 4 arquivos
assert len(os.listdir('.')) == 4
