# # 1. Faça um programa que identifique a classe social no Brasil baseada em renda de um indivíduo qualquer.
# renda = float(input("Qual é sua renda: "))
# sal = 1412

# if renda >= 15*sal:
#     print("classe a")
# elif renda > 5*sal:
#     print("classe b")
# elif renda > 3*sal:
#     print("classe c")
# elif renda > sal:
#     print("classe d")
# else:
#     print("classe e")

# # 2. Faça um programa que imprime números múltiplos de 3 em um intervalo de 0 a 1000
# for i in range(0, 1001):
#     calc = i % 3
#     if calc == 0:
#         print(i)

# # 3. Faça um programa que imprime os números primos do intervalo de 0 a 50
# for i in range(2, 51):
#     d = 0
#     for j in range(2, i-1):
#         if i%j == 0:
#             d +=1
#         if d == 0:
#             print(i)

# # 4. bhaskara
# from math import sqrt

# a = float(input())
# b = float(input())
# c = float(input())

# delta = b**2 - 4*a*c

# if delta > 0:
#     print(f"as raizes são {(-b + sqrt(delta)) / 2*a} e {(-b - sqrt(delta)) / 2*a}")
# elif delta == 0:
#     print(f"as raiz é {(-b + sqrt(delta)) / 2*a}")
# elif delta < 0:
#     print("não existem raizes reais")