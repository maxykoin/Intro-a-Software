# def contador(s, e, p):
#     x= 1
#     if s > e:
#         x = -1
#     for i in range(s, e+x, p*x):
#         print(i)
        
# s = int(input("Digite o inicio: "))
# e = int(input("Digite o fim: "))
# p = int(input("Digite o passo: "))

# contador(s, e, p)
def separa(nome):
    return {"primeira letra:": nome[0], "ultima letra:": nome[-1]}

nome = input("Escreva seu nome: ")
print(separa(nome))