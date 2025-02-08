# Faça um Programa que peça as quatro notas de 5 alunos, calcule
# e armazene numa lista a média de cada aluno, imprima o número
# de alunos com média maior ou igual a 7.0.

# Lista para armazenar as médias dos alunos
medias = []

# Loop para coletar as notas de 5 alunos
for aluno in range(1, 6):  # De 1 a 5
    print(f"\nAluno {aluno}:")
    notas = []  # Lista para armazenar as 4 notas do aluno
    
    # Coletando as 4 notas
    for i in range(1, 5):  # De 1 a 4
        nota = float(input(f"Digite a {i}ª nota: "))
        notas.append(nota)
    
    # Calculando a média do aluno e armazenando
    media = sum(notas) / len(notas)
    medias.append(media)

# Contando quantos alunos têm média maior ou igual a 7.0
aprovados = 0
for media in medias:
    if media >= 7.0:
        aprovados += 1

# Exibindo o resultado final
print(f"\nNúmero de alunos com média maior ou igual a 7.0: {aprovados}")
