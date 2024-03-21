while True:
    ex = int(input("Escolha o exercicio (1-7): "))
    match ex:
        case 0:
            break
        case 1:
            print("1) receber o tempo em segudos e mostrar o equivalente em horas, minutos e segundos")
            n = int(input("O tempo em segundos: "))
            h = n // 3600
            m = (n % 3600) // 60
            s = (n % 3600) % 60
            print(f"O tempo {n}s aquivale a {h:0>2}:{m:0>2}:{s:0>2}") 
        case 2:
            print("2) recebe o nome completo e devolve a abreviação")
            n = input("Qual é seu nome inteiro? ").split()
            l = []
            prep = ['de', 'da', 'dos', 'das', 'do']
            for i in range(0, len(n)):
                if n[i] in prep:
                    l.append(n[i])
                else:
                    l.append(n[i][0].upper())
            print(". ".join(l))
        case 3:
            print("3) ref bibliografica")
            n = input("Insira o nome: ")
            l = []
            if len(n) < 100:
                n = n.split()
                ultimonome = n[-1]
                n.remove(n[-1])
                
                for i in range(0, len(n)):
                    if len(n[i]) > 2:
                        l.append(n[i][0].upper())
                    else:
                        pass
                
                print(ultimonome, ". ".join(l))
            else:
                print("Inválido, valor maior que 100 caracteres")
        
        case 4:
            print("4) mostra a quantidade de vezes que uma palavra aparece")
            f = input("Escreva uma frase: ")
            l = input("Escrava uma palavra: ")
            print(f'A palavra "{l}" aparece {f.count(l)} vezes na frase')
        
        case 5:
            print("5) inserir uma frase e substitui uma palavra")
            f = input("Insira uma frase: ").lower()
            p = input("Insira a palavra que deseje substituir: ").lower()
            s = input("Qual palavra irá substitui-la: ").lower()
            print(f.replace(p, s))
        
        case 6:
            print("6) separar email de dominio")
            email = input("Insira seu email: ")
            index = email.find("@")
            print(f"{email[:index]} \n{email[index:]}")

        case 7:
            n = input("insira seu nome: ")
            e = input("insira seu endereço: ")
            t = input("insira seu telefone: ")

            info = " ".join([n, e, t])
            num = 0
            le = 0

            for i in info:
                if i.isnumeric():
                    num += 1
                elif i.isalpha():
                    le += 1
                    
            print(num, le)