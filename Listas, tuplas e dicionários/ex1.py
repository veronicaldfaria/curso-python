# 1. Utilizando listas faça um programa que faça 5 perguntas para uma
# pessoa sobre um crime.
# As perguntas são:
# ""Telefonou para a vítima?""
# ""Esteve no local do crime?""
# ""Mora perto da vítima?""
# ""Devia para a vítima?""
# ""Já trabalhou com a vítima?""

# O programa deve no final emitir uma classificação sobre a participação
# da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser
# classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
# ""Assassino"".
# Caso contrário,ele será classificado como""Inocente"".

# Lista de perguntas a serem feitas
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Contador para armazenar quantas respostas foram "sim"
quantidade_sim = 0

# Instruções iniciais
print("Responda às perguntas com 'sim' ou 'não'.")

# Fazendo as perguntas uma por uma
for pergunta in perguntas:
    resposta = input(pergunta + " ").strip().lower()
    
    # Validando a resposta para garantir que seja 'sim' ou 'não'
    while resposta not in ("sim", "não"):
        print("Resposta inválida! Digite apenas 'sim' ou 'não'.")
        resposta = input(pergunta + " ").strip().lower()
    
    # Se a resposta for 'sim', adiciona ao contador
    if resposta == "sim":
        quantidade_sim += 1

# Determinando a classificação com base na quantidade de respostas "sim"
if quantidade_sim == 2:
    classificacao = "Suspeita"
elif 3 <= quantidade_sim <= 4:
    classificacao = "Cúmplice"
elif quantidade_sim == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

# Exibindo o resultado final
print(f"\nClassificação: {classificacao}")
