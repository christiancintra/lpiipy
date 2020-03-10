def calcular_media(alunos):
    media = (nota1 + nota2) / 2
    print('A média é ', media)


alunos = {}
i = 1
while i <= 3:
    nome = input('Aluno: ')
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))

    alunos[nome] = nota1, nota2
    i += 1

calcular_media(alunos[])
print(alunos)


#  errado


