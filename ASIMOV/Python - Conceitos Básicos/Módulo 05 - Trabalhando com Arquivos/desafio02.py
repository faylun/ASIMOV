from pathlib import Path
import os

def getSize(path, depth = 1, lineSize = 0):
    for f in path.glob('*'):
        if f.is_dir() and not f.name.startswith('.'):
            fileSize = 0
            for file in f.glob('**/*'):
                if file.is_file():
                    fileSize += os.path.getsize(file)
            print('--' * lineSize, f.name, '\n\t-> ', round(fileSize / 1024 / 1024, 2), 'mb\n')
            if depth > 1:
                getSize(f, depth - 1, lineSize + 1)

getSize(Path.home() / 'Documents', 2)