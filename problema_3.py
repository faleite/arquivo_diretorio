""" Crie 10 pastas com o nome ‘pasta_n’ e dentro de cada pasta crie dois arquivos
‘arquivo_x’. Exiba toda a estrutura do diretório.
 """
import os
import os.path
import shutil
from pathlib import Path

for i in range(1, 11):
    if not os.path.exists(f'pasta_{i}'):
        os.mkdir(f'pasta_{i}')

l = [path for path in os.listdir('.')
     if os.path.isdir(path) and path != 'aulinha_1']

#  print(l)

for path in l:
    #  Path(f'{path}/arquivo_1.txt').touch()
    #  Path(f'{path}/arquivo_2.txt').touch()
    Path(os.path.join(path, 'arquivo_1.txt')).touch()
    Path(os.path.join(path, 'arquivo_2.txt')).touch()

# Exemplo de uso do join
#  print(os.path.join('/', 'pasta', 'pasta2', 'pasta3', 'xpto.txt'))
#  $ /pasta/pasta2/pasta3/xpto.txt

#  print(os.walk('.'))
# $ <generator object _walk at 0x100ce26c0>

for val in os.walk(('.')):
    print(val)
    #  break
