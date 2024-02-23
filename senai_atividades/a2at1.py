# RA 00963123
import math

# 1
ra = "00963123" 
print(ra)       

# 2
ra = input("Qual é seu RA? ") 
print(f"Seu RA é {ra}")       


# 3
ra1 = int(input("Qual é o 1º número do seu RA? "))                                         
ra2 = int(input("Qual é o 2º número do seu RA? "))
ra3 = int(input("Qual é o 3º número do seu RA? "))
ra4 = int(input("Qual é o 4º número do seu RA? "))
ra5 = int(input("Qual é o 5º número do seu RA? "))
ra6 = int(input("Qual é o 7º número do seu RA? "))
ra7 = int(input("Qual é o 7º número do seu RA? "))
ra8 = int(input("Qual é o 8º número do seu RA? "))
sum = ra1 + ra2 + ra3 + ra4 + ra5 + ra6 + ra7 + ra8 
print(sum)                                          

# 4
print(math.sqrt(ra4*ra5)) 

# 5
ra7 = int(input("Qual é o 7º número do seu RA? "))                                             
ra8 = int(input("Qual é o 8º número do seu RA? "))                                             
print(f"A hipotenusa do triângulo formado por esse digitos é de {math.sqrt(ra7**2 + ra8**2)}")

# 6
print(sum / int(len(ra)))

# 7
ra6 = int(input("Qual é o 7º número do seu RA? "))
print(f"A área do hexágono é de {3 * (ra6)**2 * math.sqrt(3) / 2}")

# 8
ra1 = int(input("Qual é o 1º número do seu RA? "))                                         
ra2 = int(input("Qual é o 2º número do seu RA? "))
print(f"A divisão inteira dos números é de {ra1 // ra2}")

# 9
ra1 = 1
ra2 = 1
ra3 = 9
ra4 = 6
ra8 = 3

print((ra2**ra3) - (ra4 * (ra8/ra1)))

# 10 
rand = input()
print(ra in rand)