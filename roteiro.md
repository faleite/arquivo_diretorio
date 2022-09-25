# Roteiro

1. os
2. os.path
3. shutil
4. Algumas atividades

## 1. import os

Fornece uma interface multiplataforma para interagir com o sistema operacional, ou seja,
permite facilitar a interação com o ‘shell’. Se quisermos listar, criar, deletar, modificar,
arquivos e diretórios, temos várias funções internas que nos permitem fazer esse tipo de operação.

Exemplos:
- listdir -> Lista os arquivos em um diretório
- rmdir -> Remove um diretório
- walk -> Cria uma relação de todos arquivos e diretórios presentes no diretório
- passado como parâmetro

## 2. import os.path

Este módulo implementa algumas funções úteis em nomes de caminho e utilização de paths.

Exemplos:
- exists -> Retorna se o arquivo ou diretório existe
- abspath -> Retorna o caminha absoluto do arquivo
- join -> Concatena paths para descrever caminhos

## 3. import shutil

O módulo shutil oferece uma série de operações de alto nível em arquivos e coleções de arquivos.
Em particular, são fornecidas funções que suportam a cópia e remoção de arquivos.

Exemplos:
- copy -> Copia um arquivo
- rmtree -> remove uma árvore de diretórios
- disk_usage -> Retorna a capacidade total/livre/usada em bytes do disco a qual o path pertence
