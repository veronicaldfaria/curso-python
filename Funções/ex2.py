# 2. Reverso do número. Faça uma função que retorne o reverso de um
# número inteiro informado. Por exemplo: 127 -> 721.

# Função que inverte um número inteiro
def inverter_numero(numero):
    return int(str(numero)[::-1])  # Converte para string, inverte e retorna como inteiro

# Solicita um número ao usuário
num = int(input("Digite um número inteiro: "))

# Chama a função e exibe o resultado
resultado = inverter_numero(num)
print(f"O reverso do número {num} é: {resultado}")