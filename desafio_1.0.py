de1 = int(input("Inofrme as horas da entrada:"))
M1 = int(input("Informe a minutagem da primeira entrada:"))
de2 = int(input("Informe as horas da segunda entrada "))
M2 = int(input("Informe a minutagem da segunda entrada"))

she = de1 + de2
mhe = M1 + M2

if she >= 60:
    she += 1
    mhe -= 60
    if she > 24:
        she -= 12
    else:

