from pathlib import Path
import os

# Retornando caminho do diretório de trabalho atual
print(Path.cwd())


# Esse caminho é absoluto
print(Path.cwd().is_absolute())


# Retornando caminho da primeira pasta
print(Path('primeira_pasta'))


# Esse caminho é absoluto
print(Path('primeira_pasta').is_absolute())


# Transformando o caminho em absoluto
print(Path.cwd() / 'primeira_pasta')
print((Path.cwd() / 'primeira_pasta').exists())

os.chdir(Path.home()) # os.chdir muda de diretório, ou seja, está indo para o diretório home.
print(Path.cwd() / 'primeira_pasta')
print((Path.cwd() / 'primeira_pasta').exists())


# Garantindo que estamos retornando o caminho para a pasta do script
print(__file__) # pega o caminho absoluto.
print(Path(__file__).is_absolute())
print(Path(__file__).parent) # pega a pasta pai que estamos. Ou seja, se estou em teste/arquivo1, ele irá pegar a pasta teste.

print(Path(__file__).parent / 'primeira_pasta')
print((Path(__file__).parent / 'primeira_pasta').exists())


# Trabalhando com partes de caminho
caminho_arquivo = Path(__file__)

print(caminho_arquivo)
print(caminho_arquivo.anchor) # pega a pasta raiz do sistema operacional.
print(caminho_arquivo.parent) # pega a pasta pai.
print(caminho_arquivo.name) # pega o nome completo da pasta/arquivo que estamos.
print(caminho_arquivo.stem) # Pega a base do nome do arquivo/pasta sem a extensão.
print(caminho_arquivo.suffix) # Pega a extensão do arquivo.
print(caminho_arquivo.drive) # Pega o nome do disco do sistema operacional.

print(caminho_arquivo.parent)
print(caminho_arquivo.parents[3]) # Uma forma mais rápida de navegar com o parent ( Ele pega as 3 pastas anteriores ).
