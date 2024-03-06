l = []
mult = []
prime = []

class err(Exception):
    pass

def primos(l):
    for i in range(2, max(l)):
        d = 0
        for j in range(2, i-1):
            if i%j == 0:
                d +=1
            if d == 0:
                return True
            else:
                return False

while True:
    try:
        q = int(input("Quantos números deseja calcular: "))
        
        if q < 2:
            raise err
            
        for i in range(0, q):
            n = float(input("Insira o valor: "))
            l.append(n)
    
    except ValueError:
        print("Valor Inválido")
    except err:
        print("Precisa de dois ou mais termos")
    else:
        break

print(l)

for i in range(len(l)):
    if l[i] < 0:
        l[i] = l[i] * -1
    
    ld = str(l[i]).split(".")
    print(ld)
    if int(ld[1])>0:
        mult.append(10**len(ld[1]))
        print(mult)
        for j in range(len(l)):
            try:
                l[j] = l[j] * max(mult)
            except ValueError:
                mult = [1]

    for k in primos(l):
        while True:
            if l[i] % k == 0:
                l[i] = l[i] / k
            else:
                break
        

print(l)