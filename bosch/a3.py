# Usando txt com o python & try and except
class NewError(Exception):
    pass

while True:
    n = input("Escreva um número inteiro: ")
    try:
        int(n)
        if n < 0:
            raise NewError
    except ValueError:
        print("Valor Inválido")
    except NewError():
        print("O número precisa ser maior que 0")
    else:
        break  

while True:
    l = input("Escreva uma letra: ")
        
    if str(l).isalpha():
        break
    else:
        print("Valor Inválido")


arq = open("./bosch/txt/a3.txt", "w")
arq.write(chr(ord(l) + n) + "\n")
arq.close()

l = print("Escreva uma letra: ")
n = print("Escreva um número: ")

arq = open("./bosch/txt/a3.txt", "a")
arq.write(chr(ord(l) + n))
arq.close()

arq = open("./bosch/txt/a3.txt", "r")
print(arq.read())
arq.close()

