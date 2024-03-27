from pathlib import Path
import shutil

Path('audios').mkdir()
Path('datasets').mkdir()
Path('docs').mkdir()
Path('imgs').mkdir()
Path('etc').mkdir()
Path('codigo').mkdir()
Path('videos').mkdir()

caminho = Path('Exercicio')
arqs = caminho.iterdir()

for arq in arqs:
    if '.py' in arq.name or '.ino' in arq.name:
        shutil.move(Path(arq), Path(f'codigo/{arq.name}'))
        print("Movendo arquivo: ", arq.name, "\nNova Pasta: ", f'codigo/{arq.name}\n')
    elif '.txt' in arq.name or '.pdf' in arq.name:
        shutil.move(Path(arq), Path(f'docs/{arq.name}'))
        print("Movendo arquivo: ", arq.name, "\nNova Pasta: ", f'docs/{arq.name}\n')
    elif '.jpeg' in arq.name or '.jpg' in arq.name:
        shutil.move(Path(arq), Path(f'imgs/{arq.name}'))
        print("Movendo arquivo: ", arq.name, "\nNova Pasta: ", f'imgs/{arq.name}\n')
    elif '.mp4' in arq.name:
        shutil.move(Path(arq), Path(f'audios/{arq.name}'))
        print("Movendo arquivo: ", arq.name, "\nNova Pasta: ", f'audios/{arq.name}\n')
    elif '.csv' in arq.name:
        shutil.move(Path(arq), Path(f'datasets/{arq.name}'))
        print("Movendo arquivo: ", arq.name, "\nNova Pasta: ", f'datasets/{arq.name}\n')
    else:
        shutil.move(Path(arq), Path(f'etc/{arq.name}'))
        print("Movendo arquivo: ", arq.name, "\nNova Pasta: ", f'etc/{arq.name}\n')
