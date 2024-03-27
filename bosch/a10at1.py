arq = open("Aula 10 - Níveis de CO2.txt", "r")
texto = arq.read()    
texto = texto[(texto.index("{")+1):texto.index("}")].strip().split("\n")
sensores = {}

for i in range(len(texto)):
    texto[i] = texto[i].strip()
    key = texto[i][1:3]
    value = texto[i][(texto[i].index("[")+1):texto[i].index("]")].strip().split(",")
    for j in range(len(value)):
        value[j] = int(value[j])
    sensores[key] = value

for k in sensores.keys():
    mean = sum(sensores[k]) / len(sensores[k])
    if mean > 450:
        print(f"{k} está com niveis altissimos de CO2 ({mean}), chamar equipe especializada para verificar a região")

arq.close()