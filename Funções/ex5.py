# 5. Crie uma função chamada contar_vogais que recebe uma string
# como parâmetro. Implemente a lógica para contar o número de vogais
# na string e retorne o total de vogais. Solicite ao usuário para inserir uma
# frase e utilize a função para contar as vogais.

# Função que conta as vogais em uma string
def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = sum(1 for letra in texto if letra in vogais)
    return contador

# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Chama a função e exibe o resultado
total_vogais = contar_vogais(frase)
print(f"A frase contém {total_vogais} vogais.")