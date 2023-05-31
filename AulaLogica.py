nota = 60
presenca = 60

if nota < 70 or presenca < 70:
    print("Você reprovou.")

    if nota < 70:
        print("tente melhorar ano que vem.")
    if presenca < 70:
        print("Você tem que frequentar as aulas.")
else:
    print("Você passou!")

    if nota == 100 and presenca == 100:
        print("Aprovado com Louvor.")
var = 3
