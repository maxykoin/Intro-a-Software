while ex != 0:
    ex = int(input("Escolha o exercicio para vizualizar (1-10): "))
    match ex:
        case 1:
            print("1) pede uma letra minuscula e a transforma em maiscula por ascii")
            n = input("Escreva uma letra minuscula: ")
            n = ord(n)
            print(chr(n-32))
            
        case 2:
            print("2) adiciona as informações em um arquivo de texto")
            nome = input("Escreva seu nome: ")
            idade = input("Escreva sua idade: ")
            email = input("Escreva seu email: ")
            texto = nome + " " + idade + " " + email

            arq = open("./bosch/txt/cadastro.txt", "a")
            arq.write(texto + "\n")
            arq.close()
            
        case 3:
            print("3) leia o txt")
            arq = open("./bosch/txt/cadastro.txt", "r")
            print(arq.read())
            arq.close()
            
        case 4:
            print("4) tratar erros de divisão")
            while True:
                try:
                    n1 = float(input("Digite o primeiro valor: "))
                    n2 = float(input("Digite o segundo valor: "))
                    n1/n2
                except (ValueError, ZeroDivisionError):
                    print("Valor Inválido")
                else:
                    pass
            print(n1/n2) 
            
        case 5:
            print("5) identificar o erro (arquivo nao existe)")
            try:
                arq = open("texto.txt", "r")
                arq.read()
                arq.close()
            except (FileNotFoundError):
                print("Esse arquivo não existe.") 
            else:
                pass
        
        case 6:
            print("6) identificar o erro (Usando w em vez de r)")
            try:
                arq = open("texto.txt", "w")
                arq.read()
                arq.close()
            except:
                print("Esse arquivo não pode ser lido")
            else:
                pass
            
        case 7: 
            try: 
                a = 5
                c = a + b
            except NameError:
                print("Valor Inválido")
            else:
                pass
            
        case 8:
            try: 
                a = 5
                b = "b"
                c = a + b
            except TypeError:
                print("Valoe Inválido")
            else:
                pass
            
        case 9:
            try:
                a = 5
                b = 5
                c = a + b
                print("{}".format())
            except IndexError:
                print("valor invalido")
            else:
                pass
            
        case 10:
            try:
                a = 5
                b = 5
                c = a + b
                print("{0}{1}{}".format(a, b, c))
            except ValueError:
                print("valor inválido")
            else:
                pass
        case 0:
            break