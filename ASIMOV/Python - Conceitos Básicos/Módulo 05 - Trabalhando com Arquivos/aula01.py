from pathlib import Path

path = Path('primeiro_arquivo/segundo_arquivo')
path2 = Path('terceiro_arquivo') / Path('quarto_arquivo')

print(path)
print(Path.home())
print(path2)