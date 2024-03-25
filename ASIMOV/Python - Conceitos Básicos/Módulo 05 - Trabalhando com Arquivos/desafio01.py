# Desenvolva um script para encontrar um arquivo dentro da pasta home do usuário

from pathlib import Path
import os
def fileList(path, file):
    for f in path.glob('**/*'):
        if f.is_file():
            if f.stem == file:
                print(f)
fileList(Path.cwd(), 'aula01')