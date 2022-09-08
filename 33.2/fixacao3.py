reprovados = []

with open("alunos.txt", 'r') as file:
    for line in file:
        grade = line.split(" ")
        if int(grade[1]) < 6:
            reprovados.append(grade[0] + "\n")

with open("reprovados.txt", 'w') as reprovadoss:
    reprovadoss.writelines(reprovados)
