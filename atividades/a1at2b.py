# Faça um programa que calcule as raízes de um polinômio de segunda ordem via fórmula de Bhaskara. Considere que as raízes sejam reais.
import math # importa a biblioteca integrada do python (numpy não rodou)

# atribui os valores do polinômio a variáveis
a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

delta = (b**2) - (4*a*c) # calcula o delta
x1 = (-b + math.sqrt(delta)) / (2*a) # calcula a primeira raiz fazendo uso da função de raiz quadrada da biblioteca
x2 = (-b - math.sqrt(delta)) / (2*a) # calcula a segunda raiz fazendo uso da função de raiz quadrada da biblioteca

print(f"As raízes dessa equação de segundo grau é de {x1} e {x2}") # print dos resultados