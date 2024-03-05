while True:
    ex = int(input("Escolha o exercicio: "))
    match ex:
        case 0:
            break
        case 1:
            n1 = float(input("Primeiro número: "))
            n2 = float(input("Segundo número: "))
            
            if n1 > n2:
                print(n1)
            elif n2 > n1:
                print(n2)
            else:
                print("Valores iguais")
        case 2:
            l = input("Insira seu genero (M/F): ").upper()
            
            if l == "M":
                print("Masculino")
            elif l == "F":
                print("Feminino")
            else:
                print("Caractere inválido")
        case 3:
            n1 = float(input("1º: "))
            n2 = float(input("2º: "))
            n3 = float(input("3º: "))
            
            print("Menor:")
            if n1 < n2 and n1 < n3:
                print(n1)
            elif n2 < n1 and n2 < n3:
                print(n2)
            elif n3 < n1 and n3 < n2:
                print(n3)
            
            print("Maior")
            if n1 > n2 and n1 > n3:
                print(n1)
            elif n2 > n1 and n2 > n3:
                print(n2)
            elif n3 > n1 and n3 > n2:
                print(n3)
        
        case 4:
            n = int(input("Número inteiro menor que 1k: "))
            if n < 1000 and n > 100:
                print(f"{n // 100} centenas, {n % 100 // 10} dezenas, {n % 10} unidades")
            elif n < 100 and n > 10:
                 print(f"{n % 100 // 10} dezenas, {n % 10} unidades")
            else:
                print("Valor Inválido")
                
        case 5:
            p = float(input("Quantida de de kWh: "))
            i = input("Tipo de instalação (R/I/C): ").lower()
            
            if i == "r":
                if p <=500:
                    print(f"Valor a pagar: R${0.4 * p:.2f}")
                elif p>500:
                    print(f"Valor a pagar: R${0.65 * p:.2f}")
            elif i == 'c':
                if p <=1000:
                    print(f"Valor a pagar: R${0.55 * p:.2f}")
                elif p>1000:
                    print(f"Valor a pagar: R${0.6 * p:.2f}")
            elif i == "i":
                if p <=5000:
                    print(f"Valor a pagar: R${0.55 * p:.2f}")
                elif p>5000:
                    print(f"Valor a pagar: R${0.6 * p:.2f}")
            else:
                print("Instalação desconhecida")
        
        case 6:
            class Error(Exception):
                pass
            class err(Exception):
                pass
            
            lista = ["+", "-", "*", "/"]
            
            
            try:
                n1 = float(input("1º: "))
                n2 = float(input("2º: "))
                
                op = input("+, -, *, /")
                
                if op not in lista:
                    raise Error
                elif op == "+":
                    print(n1+n2)
                elif op == "-":
                    print(n1-n2)
                elif op == "*":
                    print(n1*n2)
                elif op == "/":
                    if n2 < 0:
                        raise err
                    print(n1/n2)
                    
            except Error:
                print("Simbolo Invalido")
            except ValueError:
                print("Valor Inválido")
            except err:
                print("Valor menor que 0")
        
        case 7:
            pass
        
        case 8:
            while True:
                n = int(input("Digite uma nota: "))
                
                if n > 0 and n <=10:
                    print("ok")
                    break
                else:
                    print("Valor Inválido")
        
        case 9:
            n = int(input("Número: "))
            
            for i in range (11):
                print(f"{n} x {i} = {n*i}")
        
        case 10:
            n = int(input("Número: "))
            s = int(input("Inicio: "))
            f = int(input("Fim: "))
            
            for i in range(s, f):
                print(f"{n} x {i} = {n*i}")
            
        case 11:
            n = int(input("Número: "))
            r = 1
            for i in range(1, n+1):
                r = r * i
                print(r)
        
        case 12:
            c=0
            s=0
            while True:
                n = int(input("Digite um número inteiro: "))
                s += n
                c += 1
                
                if n == 0:
                    c -= 1
                    break
            
            print(f" Quantidade de números digitados: {c} \n Soma: {s} \n Média: {s/c}")
        
        case 13:
            pass
        
        case 14:
            pass
        
        case 15:
            import random 
            
            while True:
                ns = random.randint(1, 101)
                
                try:
                    p = int(input("Digite seu palpite (1-100): "))
                except ValueError:
                    print("Valor Inválido")
                
                if p == ns:
                    print("você acertou!")
                    break
                elif p > ns:
                    print("está acima")
                elif p < ns:
                    print("está abaixo")
        
        case 16:
            pass
            b = int(input("Base: "))
            e = int(input("Expoente: "))
            
            print()
            
        case 17:
            pass
        
        case 18:
            pass
        
        case 19:
            pass
        
        case 20:
            import random
            l1 = []
            l2 = []
            
            for i in range(0, 11):
                l1.append(random.randint(0, 11))
                l2.append(random.randint(0, 11))
            
            print(l1)
            print(l2)
            
            for i in range(0, len(l1)):
                if l1[i] == l2[i]:
                    print(f"{i} está nas duas listas")
                else:
                    pass
                    
        case 21:
            pass
        
                