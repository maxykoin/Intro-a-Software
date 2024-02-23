# Com base no que foi apresentado anteriormente, crie um programa que você deve digitar os seguintes dados: nome, altura, peso e idade. 
# O programa deve imprimir uma frase contendo estas informações.

nome = input("Qual é seu nome? ") # pergunta o nome od usuário
altura = int(input("Qual é sua altura? ")) # pergunta a altura do usuário e considera somente números inteiros
peso = float(input("Qual é seu peso? ")) # pergunta o peso do usuário e considera números com virgula
idade = int(input("Qual é sua idade? ")) # pergunta a idade do usuário e considera somente números inteiros

print(f"Olá {nome}! Você mede {altura}cm, pesa {peso}Kg e tem {idade} anos")