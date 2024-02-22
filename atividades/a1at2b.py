# Faça um programa que calcule as raízes de um polinômio de segunda ordem via fórmula de Bhaskara. Considere que as raízes sejam reais.
import math

a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

delta = (b**2) - (4*a*c)
x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)

print(f"As raízes dessa equação de segundo grau é de {x1} e {x2}")