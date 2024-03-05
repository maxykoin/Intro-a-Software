# n = int(input("Digite o limite: "))
# sum = 0

# print("0", end='')
# for i in range(1, n+1):
#     print(f" + {i}", end = '')
#     sum += i 

# print(f" = {sum}")

n = int(input("Insira o valor: "))

# for i in range(0, n):
#         print("x "*n)

for i in range(n):
        for j in range(n):
                print("x ", end='')
        print("\n", end='')