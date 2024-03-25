from pathlib import Path
import shutil
import os


# Copiando arquivo com copyfile - Não copia as permissões
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_arquivo_destino = pasta_atual / 'destino1' / 'texto.txt'

shutil.copyfile(caminho_arquivo, caminho_arquivo_destino)


# Copiando arquivo com copy - Copia as permissões
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino2'

shutil.copy(caminho_arquivo, caminho_pasta_destino)


# Copiando arquivo com copy2 - copia as permissões e os metatados
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino3'

shutil.copy2(caminho_arquivo, caminho_pasta_destino)


# Movendo arquivos
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino1'

shutil.move(caminho_arquivo, caminho_pasta_destino)


pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_arquivo_destino = pasta_atual / 'destino2' / 'texto.txt'

shutil.move(caminho_arquivo, caminho_arquivo_destino)


# Deletando arquivos
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_arquivo_destino = pasta_atual / 'destino3' / 'texto.txt'
shutil.copyfile(caminho_arquivo, caminho_arquivo_destino)


if caminho_arquivo.exists():
    os.remove(caminho_arquivo)
