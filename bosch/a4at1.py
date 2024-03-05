import math
ex = -1

while ex != 0:
    ex = int(input("Escolha o exércicio (1-3): "))
    match ex:
        case 0:
            break
        case 1:
            print('='*10, "Jogo de Adivinhação", "="*10)
            ns = 42
            try:
                p = int(input("Digite seu palpite: "))
            except ValueError:
                print("Valor Inválido")
            else:
                if p == ns:
                    print("Você acertou!")
                else:
                    print("Você errou.")

        case 2:
            print('='*10, "Eleição", "="*10)
            ano = int(input("Ano de nascimento: "))
            idade = 2024 - ano
            print(f"Você tem {idade} anos")
            if idade <= 16:
                print("Não é permitido votar!")
            elif idade<=18 or idade>=70:
                print("Seu voto é facultativo")
            else:
                print("Seu voto é obrigatório!")

        case 3:
            class ModuleError(Exception):
                pass

            print('='*10, "Calculadora", "="*10)
            num = int(input(" 1) Números Reais \n 2) Números complexos \n Resposta: "))

            if num == 1:
                op = int(input("""Escolha uma operação:
                            [1] Soma
                            [2] Subtração
                            [3] Multiplicação
                            [4] Divisão
                            [5] Potênciação
                            [6] Radiciação
                            Resposta: """))
                try:
                    n1 = float(input("Primeiro valor: "))
                    n2 = float(input("Segundo valor/expoente/divisor: "))
                except ValueError:
                    print("Valor Inválido")

                match op:
                    case 1:
                        print(f"A soma dos dois valores é de {n1+n2}")
                    case 2:
                        print(f"A subtração dos dois valores é de {n1-n2}")
                    case 3:
                        print(f"A multiplicação dos dois valores é de {n1*n2}")
                    case 4:
                        print(f"A divisão dos dois valores é de {n1/n2}")
                    case 5:
                        print(f"A potência dos dois valores é de {n1**n2}")
                    case 6:
                        print(f"A radiciação dos dois valores é de {n1**(n2**-1)}")
                
            elif num == 2:
                op = int(input("""Escolha uma operação:
                            [1] Conversão Retângular -> Polar
                            [2] Conversão Polar -> Retângular
                            [3] Soma
                            [4] Multiplicação
                            [5] Divisão
                            Resposta: """))
            
                match op:
                    case 1:
                        try:
                            n1 = float(input("Real: "))
                            n2 = float(input("Imaginário: "))
                        except ValueError:
                            print("Valor Inválido")
                            
                        pol = math.sqrt(n1**2 + n2**2)
                        ang = math.degrees(math.atan2(n2, n1))

                        print(f"{round(pol,3)}∠{ang}º")
                    case 2:
                        try:
                            n1 = float(input("Real: "))
                            n2 = float(input("Imaginário: "))
                            if n2 < 0:
                                raise ModuleError
                        except ValueError:
                            print("Valor Inválido")
                        except ModuleError:
                            print("O valor tem que ser o modulo do ângulo")

                        real = n1 * math.cos(n2)
                        img = n1 * math.sen(n2)

                        print(f"{real} + {img}j")
                    case 3:
                        try:
                            n1 = float(input("1º Real: "))
                            n2 = float(input("1º Imaginário: "))
                            n3 = float(input("2º Real: "))
                            n4 = float(input("2º Imaginário: "))
                        except ValueError:
                            print("Valor Inválido")
                        
                        real = n1+n3
                        img = n2+n4
                        print(f"{real} + {img}j")
                    case 4:
                        try:
                            n1 = float(input("1º Real: "))
                            n2 = float(input("1º Imaginário: "))
                            n3 = float(input("2º Real: "))
                            n4 = float(input("2º Imaginário: "))

                            if n2<0 or n4<0:
                                raise ModuleError
                        except ValueError:
                            print("Valor Inválido")
                        except ModuleError:
                            print("O valor tem que ser o modulo do ângulo")

                        real = n1*n3
                        img = n2+n4
                        print(f"{real}∠{img}º")
                    case 5:
                        try:
                            n1 = float(input("1º Real: "))
                            n2 = float(input("1º Imaginário: "))
                            n3 = float(input("2º Real: "))
                            n4 = float(input("2º Imaginário: "))

                            if n2<0 or n4<0:
                                raise ModuleError
                        except ValueError:
                            print("Valor Inválido")
                        except ModuleError:
                            print("O valor tem que ser o modulo do ângulo")

                        real = n1/n3
                        img = n2-n4
                        print(f"{real}∠{img}º")