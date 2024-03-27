from pathlib import Path
import shutil

class CharacterError(Exception):
    pass

while True:
    try:
        pasta = input("Digite o nome de uma pasta a ser criada: ")
        if not pasta.isalnum():
            raise CharacterError
        Path(pasta).mkdir()
    except CharacterError:
        print("Nome inválido! Tente novamente!")
    except FileExistsError:
        print("Essa pasta já existe!")
    else:
        print("Pasta criada com sucesso")
        break

while True:
    try:
        arq = input("Qual arquivo você deseja mover: ")
    except FileNotFoundError:
        print("Esse arquivo não existe!")
    else: 
        shutil.move(Path(arq), Path(Path(pasta) / arq))
        print("Arquivo movido com sucesso")
        break