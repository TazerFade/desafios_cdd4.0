de1 = int(input("Informe as horas da entrada:"))
M1 = int(input("Informe a minutagem da primeira entrada:"))
de2 = int(input("Informe as horas da segunda entrada: "))
M2 = int(input("Informe a minutagem da segunda entrada: "))

Sf = 0

# Ajuste para formato 12h e definição de AM/PM
if de1 >= 12:
    if de1 > 12:
        de1 -= 12
    periodo1 = "PM"
else:
    if de1 == 0:
        de1 = 12
    periodo1 = "AM"

if de2 >= 12:
    if de2 > 12:
        de2 -= 12
    periodo2 = "PM"
else:
    if de2 == 0:
        de2 = 12
    periodo2 = "AM"

# Soma das horas e minutos
Sf = de1 + de2
Mf = M1 + M2

# Se a soma dos minutos passar de 60, ajustar corretamente
if Mf >= 60:
    Mf -= 60
    Sf += 1

# Se a soma das horas ultrapassar 12, ajustar corretamente
if Sf > 12:
    Sf -= 12

# Definir o período final (AM/PM) com base no contexto
if periodo1 == "PM" or periodo2 == "PM":
    periodo_final = "PM"
else:
    periodo_final = "AM"

# Ajuste para sempre exibir os minutos com dois dígitos
if Mf < 10:
    print(f"Horário final foi: {Sf}:0{Mf} {periodo_final}")
else:
    print(f"Horário final foi: {Sf}:{Mf} {periodo_final}")
