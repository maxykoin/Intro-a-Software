while True:
    n1 = float(input("Primeiro valor: "))
    n2 = float(input("Segundo valor: "))
    c = int(input("Escolha uma operação: \n [1] Soma \n [2] Subtração \n [3] Multiplicação \n [4] Divisão \n [0] Sair"))
    if c == 1:
        print(f"A soma dos dois valores é de {n1+n2}")
    if c == 2:
        print(f"A subtração dos dois valores é de {n1-n2}")
    if c == 3:
        print(f"A multiplicação dos dois valores é de {n1*n2}")
    if c == 4:
        print(f"A divisão dos dois valores é de {n1/n2}")
    if c == 0:
        break
