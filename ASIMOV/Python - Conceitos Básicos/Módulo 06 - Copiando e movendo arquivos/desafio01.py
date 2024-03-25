from pathlib import Path
import shutil
import datetime

main_path = Path(__file__).parent / 'arquivos_desafio'
create_dir = Path(__file__).parent / 'organized_files'
backup = Path(__file__).parent / 'backup'

backup.mkdir(exist_ok=True)

for f in main_path.glob('**/*'):
    folder_organized = Path(create_dir / f.suffix.replace('.', ''))
    folder_organized.mkdir(exist_ok=True)

    if f.suffix.replace('.', '') != '':
        shutil.move(str(main_path / f.name), str(create_dir / f.suffix.replace('.','')))
    else:
        shutil.move(str(main_path / f.name), str(create_dir / f.name))

time_now = datetime.datetime.now().strftime('%Y_%m_%d')
shutil.make_archive(backup / time_now, 'zip', create_dir)