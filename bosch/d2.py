from datetime import datetime
d = datetime.now()

dias = {1:31, 2:30, 3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:30,11:30,12:31}
meses = {1:'janeiro',2:'fevereiro',3:'março',4:'abril',5:'maio',6:'junho',7:'julho',8:'agosto',9:'setembro',10:'outubro',11:'novembro',12:'dezembro'}

class Error(Exception):
    pass

class YearError(Exception):
    pass

class MonthError(Exception):
    pass

class DayError(Exception):
    pass

while True:
    try:
        data = input("Digite sua data de nascimento (dd/mm/aaaa): ").split('/')
        for i in range(len(data)):
            if data[i].isdigit() == False:
                raise Error
            else:
                data[i] = int(data[i])

        if len(str(data[0])) > 2 or len(str(data[1])) > 2 or len(str(data[2])) > 4:
            raise Error
        else:
            if data[2] < 1874 or data[2] > d.year:
                raise YearError
            else:
                if data[1] > 12 or data[1] < 1:
                        raise MonthError
                else:
                    if data[0] < 1:
                        raise DayError
                
                    if data[1] == 2:
                        if data[2] % 4 == 0:
                            dias[2] = 28
                            if data[0] > 29:
                                raise DayError
                        else:
                            dias[2] = 29
                            if data[0] > 28:
                                raise DayError
                            
                    dia = dias[data[1]]

                    if data[0] > dia:
                        raise DayError 
    except Error:
        print("-> A data deve ser no formato dd/mm/aaaa")
    except YearError:
        print("-> Ano Inválido")
    except MonthError:
        print("-> Mês Inválido")
    except DayError:
        print("-> Dia Inválido")
    else:
        break

if data[0] == d.day and data[1] == d.month and data[2] == d.year:
    print("Você nasceu hoje!")
elif data[0] == d.day and data[1] == d.month:
    print("Feliz aniversário!")
else:
    print(f"Hoje é dia {d.day} de {meses[d.month]} de {d.year}\nVocê nasceu no dia {data[0]} de {meses[data[1]]} de {data[2]}")

if data[1] < d.month:
    if data[0] <= d.day:
        print(f"Você tem {d.year-data[2]} anos, {d.month-data[1]} meses e ", end='')
        print(f"{d.day - data[0]} dias")
    elif data[0] > d.day:
        print(f"Você tem {d.year-data[2]} anos, {d.month-data[1]-1} meses e ", end='')
        print(f"{d.day+dias[data[1]]-data[0]} dias")
elif data[1] > d.month:
    print(f"Você tem {d.year-data[2]-1} anos, {12+d.month-data[1]} meses e ", end='')
    if data[0] < d.day:
        print(f"{d.day - data[0]} dias")
    elif data[0] > d.day:
        print(f"{d.day+dias[data[1]]-data[0]} dias")
elif data[1] == d.month:
    print(f"Você tem {d.year-data[2]-1} anos, {12+d.month-data[1]} meses e ", end='')
    if data[0] < d.day:
        print(f"{d.day - data[0]} dias")
    elif data[0] > d.day:
        print(f"{d.day+dias[data[1]]-data[0]} dias")