while True:
    ex = int(input("Escolha um exercício (1-8): "))

    match(ex):
        case 0:
            break
        case 1:
            print("-"*10, "Exercício 1", "-"*10)
            n = input("Insira seu nome: ")
            ra = input("Insira seu RA: ")
            cpf = input("Insira seu CPF: ")
            cel = input("Insira seu celular: ")

            tul = (n, ra, cpf, cel)
            print(tul)
        case 2:
            num = []
            print("-"*10, "Exercício 2", "-"*10)
            for i in range(0, 51, 3):
                num.append(i)
            print(num)

        case 3:
            m = [[2, 5], [3, -4]]
            d1 = 1
            d2 = 1
            print("-"*10, "Exercício 3", "-"*10)

            for i in range(len(m)):
                for j in range(len(m[i])):
                    if i == j:
                        d1 *= m[i][j]
                    else:
                        d2 *= m[i][j]
            print(d1 - d2)
        case 4:
            print("-"*10, "Exercício 4", "-"*10)

            def soma(x, y):
                return x+y
            def subt(x, y):
                return x-y
            def mult(x, y):
                return x*y 
            def div(x, y):
                return x / y
                
            op = input("1- Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n")
            n1 = float(input("1º: "))
            n2 = float(input("2º: "))

            if op == "1":
                 print(soma(n1, n2))
            elif op == "2":
                 print(subt(n1, n2))
            elif op == "3":
                 print(mult(n1, n2))
            elif op == "4":
                 print(div(n1, n2))
        case 5:
            print("-"*10, "Exercício 5", "-"*10)
            def square(l):
                return l**2

            def triangle(b, h, l):
                return (b * h / 2) * l  

            def circle(pi, r):
                return pi * r**2
            
            op = input("Qual forma deseja calcular:\n1-Quadradro\n2-Triângulo\n3-Círculo\n")

            match(op):
                case 1:
                    l = float(input("Valor do lado: "))
                    print("Área: ", square(l))
                case 2:
                    b = float(input("Valor da base: "))
                    h = float(input("Valor da altura: "))
                    l = float(input("Valor do lado: "))
                    print("Área:", triangle(b, h, l))
                case 3:
                    pi = float(input("Valor de pi: "))
                    r = float(input("Valor do raio: "))
                    print("Área: ", circle(pi, r))
        case 6:
            print("-"*10, "Exercício 6", "-"*10)
            n = input("Insira seu nome: ")
            cpf = input("Insira seu CPF: ")
            cel = input("Insira seu celular: ")
            
            info = {'nome': n, 'cpf': cpf, 'celular': cel}

            op = input("Qual informação você deseja ver: ").lower()

            print(info[op])
        case 7:
            print("-"*10, "Exercício 7", "-"*10)
            chamada = []

            a = int(input("Quantos alunos tem na sala? "))

            for i in range(a):
                n = input("Insira o nome: ")
                ra = input("Insira o RA: ")
                pres = input("Presente? ")
                chamada.append({"nome": n, "ra": ra, "presente": pres})

            for j in range(a):
                print(chamada[j])
        
        case 8:
            from random import randint
            tries = 0
            pont = []

            while True:
                j = input("Qual é seu nome? ")
                numC = 11 # randint(0, 100)
                randint(0, 100)

                while True:
                    numJ = int(input("Escolha um número inteiro (0-100): "))

                    if numJ > numC:
                        print("Mais baixo")
                        tries += 1
                    elif numJ < numC:
                        print("Mais alto")
                        tries += 1
                    elif numJ == numC:
                        if tries == 0:
                            pont.append({"Jogador": j, "Tentativas": tries+1})
                            tries = 0
                            break
                        else:
                            pont.append({"Jogador": j, "Tentativas": tries})
                            tries = 0
                            break
                
                
                print("\n{:^35}".format("PONTUAÇÃO"))
                for i in pont: 
                    print(f"| Jogador: {i["Jogador"]} | Pontuação: {i["Tentativas"]} |")

                a = int(input("\nDeseja jogar novamente (1-Sim/2-Não)? "))

                if a == 2:
                    break