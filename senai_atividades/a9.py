while True:
    ex = int(input("\nEscolha um exercício: "))
    match ex:
        case 0:
            break

        case 1:
            print("1) Inverter o conteúdo de uma lista")
            lista = [1,3,5,2,94,7,8,8,7,7]

            def remove(lista):
                return lista.pop()
            
            for i in range(len(lista)):
                print(remove(lista), end= " ")
        
        case 2:
            print("2) Imitar o sistema de senhas de um fast food")
            from random import randint
            senha = []
            cliente = []
            pedido = {}

            def add(lista, valor):
                return lista.append(valor)
            
            def remove(lista):
                return lista.pop(0)

            for i in range(10):
                add(cliente, randint(1, 99))
                add(senha, randint(100, 999))

            for i in cliente:
                print(f"Cliente: {i} | Pedido: {remove(senha)}")

