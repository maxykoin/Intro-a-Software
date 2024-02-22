# pra implementar no geometria espacial

import math
import sympy

r = float(input("raio "))
h = float(input("altura "))
p = int(input("O π é: \n 1- Valor Integral \n 2- Valor Definido \n 3- Indefinido \n Respostas: "))

def areaCilindro(r, h, p):
    return 2*p*r*h + 2*p

match p: 
    case 1: 
        print(areaCilindro(r, h, math.pi))
    case 2:
        p = float(input("Valor de π "))
        print(areaCilindro(r, h, p))
    case 3:
        print(areaCilindro(r, h, sympy.pi))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             