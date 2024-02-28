# Usando txt com o python & try and except
while True:
    n = input("Escreva um número: ")
    try:
        int(n)
    except ValueError:
        print("Valor Inválido")
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

